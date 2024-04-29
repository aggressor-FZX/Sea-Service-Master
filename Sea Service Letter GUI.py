
import sys
import os
from os.path import exists
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from  UI_Top_level_Class import Ui_SeaServiceMaster
import pathlib as pt
import pandas as pd
import Make_PDF as make_word_doc
#import pdb


class Ui_SeaServiceMaster(QMainWindow, Ui_SeaServiceMaster):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #the connections from button ##
        #update lower left color table view, follws the Make Table View pathway
        self.Lastname.editingFinished.connect(self.change_name)
        self.create_letter.clicked.connect(self.generate_letter)
        #the set up file pathway - "file download" -> open_file->make_table->create_tables->sort_days
        self.load_file.clicked.connect(self.calander_table_pathway)
        #The Make  Letter Table Pathway
        #sort days to to letter table (calls update sections) then letter table to set data.
        self.make_table_button.clicked.connect(self.letter_table_pathway)
        #changes the sort of table that is shown
        self.InportTimeLetter.toggled.connect(self.update_letter_table)
        self.INFOBOX.setText("Select a last name to enable Load File")
        self.reset()
        
    def reset(self):
        # set all members to their initial value
        # things retained by the application and used below 
        # Reset method to set everything back to square one
        self.day_segment = None
        self.u_w_days = None
        self.user_arg = self.update_selections()
        self.d_frame = "no data yet"
        self.file_path = "not yet set"
        self.test_path = r"\\omao.noaa.local\ODNetshares\Command\JO\test"
        self.name = None
        self.dates = None
        self.data = None
        self.model = None
        self.columns = None
        self.word_rows  = None
        self.tableWidget.installEventFilter(self)
        self.program_directory = QFileDialog().directory().absolutePath()
        self.tableview_rows = None
        self.index = None #used index rather than name since columns keys have \n in the full names
        self.total_days = 0
        self.headers = None
        self.table_cols =  None
        self.table_num_rows = None 
        self.table_num_cols = None       
        
    def error_input(self,  input):
        self.INFOBOX.setText("Can't parse: ",  str(input))
        return
        
    def cell_changed(self,  item):#changing the  vaules in Begin, end and cred/u/w days 
        head= [x for x in self.table_cols.keys()]# means we go thru and update day sum
        row = item.row()
        column = item.column()
        print("regestered a change in " ,  item.text(), head[column])
        if head[column] == head[-1]: # is it the last column (row day sum)
            print('last column changed, updating toTal',  head[column])
            days = self.update_table_total()
            if  days  == self.total_days:#check sum day
                print('no change in total return')
                return#return if no change
            
            
        elif head[column] == 'Begin Date':#the begun date is minus from end date
            if self.tableWidget.item(row, column+1): #End date is not None
                date = self.tableWidget.item(row, column).text()
                date = pd.to_datetime(date, errors='coerce')
                if date == 'NaT' :
                    self.error_input(date)
                    return
                e_date= self.tableWidget.item(row, column+1).text()
                e_date = pd.to_datetime(e_date)
                delta = e_date - date + pd.Timedelta(days=1)# get a new day delta, add 1 to count last day
                if self.tableWidget.item(row, column+2) != None: #'days u/w not empty'
                    
                    if str(delta.days) != self.tableWidget.item(row, column+2).text():#check sum for change
                        new_label = QTableWidgetItem(str(delta.days))
                        self.tableWidget.setItem(row, column+2, new_label)#set new row sum
                        days = self.update_table_total()#update total
                        print("adding days to column number of days",  days)
                    else:
                        return #value is the same change nothing
                else: #otherwise update the day and recalculate the sum of all deltas
                    print("this sum u/w cell was none (empty)")
                    new_label = QTableWidgetItem(str(delta.days))
                    self.tableWidget.setItem(row, column+1, new_label)
                    days = self.update_table_total()
                    print("days value changed",  days)
                    return # if it hasn' changed, leave it and return. 
                   
            else:
                print('begin date + 1 column (End date) was none')
                return# can't subtract from None object
            
        elif head[column] =='End Date':# the begin date is subtracted from end
            print('end date column was changed')
            date = self.tableWidget.item(row, column).text()#get date
            if date == 'Total:':
                print('reached Total cell no update needed')
                return 
            date = pd.to_datetime(date, errors='coerce')
            if date == 'NaT' :
                self.error_input(date)
                return
            b_date= self.tableWidget.item(row, column-1).text()#get begin date
            b_date = pd.to_datetime(b_date)#turn it into a date object
            delta = date - b_date  + pd.Timedelta(days=1)#get the diff , add one to count last day
            print(date,  b_date,  delta)

            if self.tableWidget.item(row, column+1) != None: #day u/w column is not empty
                #since not empty we add it and recalculate days
                print('day u/w column (or last col) is not empty')
                if str(delta) != self.tableWidget.item(row, column+1).text():#check sum day
                    new_label = QTableWidgetItem(str(delta.days))
                    self.tableWidget.setItem(row, column+1, new_label)
                    days = self.update_table_total()   
                else:
                    return#return if no chanage in sum 
            else:#day u/w column is None (blank) so recaluclate with new delta
                print('column row is empty ',  "end date column")
                new_label = QTableWidgetItem(str(delta.days))
                self.tableWidget.setItem(row, column+1, new_label)
                days = self.update_table_total()
            
            #we c ompare it with the stored value of the total. If it changed, we update it.
            if  self.update_table_total() == self.total_days:#check sum day
                print('no change in total return')
                return#return if no change
            else:
                print('total was changed, updating')
                days = self.update_table_total()
                
            
        else: #changing other items does nothing
            print('changed N/A column no math to do')
            return
            
         #set the total cell (if we made it here the total has changed)  
        self.total_days = days #update the stored value. (will go on forever if you don't update)
        total = QTableWidgetItem(days)
        self.tableWidget.setItem(self.table_num_rows, self.table_num_cols-1,  total)#put back in table
        
    def update_table_total(self):
        rows = self.table_num_rows
        cols = self.table_num_cols
        self.headers[cols-1] #get last column 'Days Underway'
        print('last column for update is :',  self.headers[cols-1] )
        day_filter  = filter(None, [self.tableWidget.item(x, cols-1).text() for x in range(rows) if self.tableWidget.item(x, cols-1) != None ])   
        #we are adding the numbers in one column,  filter out None types
        days = sum([int(x) for x in day_filter])#now add the days together
        print('old day count: ', self.tableWidget.item(rows, cols-1).text())#old value
        print('New day, row, col; ', days,  rows-1,  cols-1)
        #return sum as a sting type value
        return str(days)
        
    def letter_table_pathway(self):
        print('letter table path')
        self.sort_days()
        print('sorted days, letter table next')
        self.letter_table()
        print('setting date')

        self.letter_set_data()
        print('enable letter button')
        self.create_letter.setEnabled(True)
        
    def calander_table_pathway(self,  shortcut=False):    
        if not shortcut:
            print("path not on file, open dialog")
            self.set_up_file_download()
        print('opening file')
        self.open_file()
        print('data prep')
        self.data_prep()
        if self.tableview_rows == None: #returns none if name not found
            return self.INFOBOX.setText(" Name not found")
        print("making LCD")
        self.make_lcd()
        print('making table')
        self.create_tables()
        self.make_table_button.setEnabled(True)
        
    def change_name(self): #checks name and runs the calender table path way.
        self.name = self.Lastname.text()
        if self.name.isalpha():
            self.load_file.setEnabled(True)
        else:
            return self.INFOBOX.setText("Letters Only")
        #if we already have file, use it 
        if  self.file_path == "not yet set":
            print('no path on file')
            return
        else:# reset data values if data exist and must change to a new name
            save = self.file_path
            name = self.name
            self.reset()
            self.file_path = save
            self.name = name
            self.calander_table_pathway(True)
            if self.model == None:
                return
            else:
                print('updating letter table')
                self.update_letter_table()
            
            
    def recreate_table(self):
        #Letter table
        print('recreating letter tabel')
        del self.tableWidget
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QRect(10, 80, 851, 241))
        self.tableWidget.eventFilter
        
    def update_letter_table(self):
        print('update_letter table')
        if self.file_path == "not yet set": #must have file
            return
        if self.data == None: #must have file
            return
        elif self.model == None: #must have table to update
            return
        elif self.columns == None: #must have data
            return
        else:
            print('recreating the table in update letter table')
            self. recreate_table()
            self.user_arg = self.update_selections()
            self.letter_table_pathway()
            
    def generate_letter(self):
        
        self.user_arg = self.update_selections()

        self.ms_word_dict()
        
        if not exists(self.file_path):
            return self.INFOBOX.setText("choose a source file please")
        #serach local path 
        #looks for Template folder
        
        root_dir = pt.Path(os.getcwd()).resolve()
        temp_dir = root_dir.joinpath("Template_Folder")
        #out_dir = root_dir.joinpath("Generated_"+self.name+".docx")
        
        save_dir = QFileDialog.getExistingDirectory(
            self, "SAVE DIRECTORY?",
            self.program_directory,
            QFileDialog.ShowDirsOnly)
            
        save_dir = pt.Path(save_dir)
        
        temp_dir = QFileDialog.getExistingDirectory(
            self, "TEMPLATE DIRECTORY",
            self.program_directory,
            QFileDialog.ShowDirsOnly)
        if len(self.user_arg) < 18:
            self.INFOBOX.setText("Fill Out All Fields!")
            print(self.user_arg)
        temp_dir = pt.Path(temp_dir)
        self.INFOBOX.setText("Processing")

        make_word_doc.printer(self.user_arg, self.word_rows, temp_dir, self.total_days, save_dir)
        return
        
     #updates the stored values by reading what is in the letter boxes   
    def update_selections(self):#method returns updated dictionary with user inputs
        self.user_arg = None
        dict = {}
        dict["Last Name"] = self.Lastname.text()
        dict["Full Name"] = self.fullname.text()
        dict["Title"] = self.pos_title.text()
        dict["Type"] =  self.office_type.currentText()
        dict["CO Name Rank"] =   self.co_namerank.text()
        dict["Reference#"] = self.refnum.text()
        dict["Inport Letter"] = self.InportTimeLetter.isChecked()
        dict["Ship Name"] =  self.ShipName.text()
        dict["GRT"] = self.grt_lineedit.text()
        dict["Propulsion"] = self.prop.text()        
        dict["Nature"] = self.nature.text()   
        dict["Type Days"] = self.Typedays.text()
        dict["Ship Number"] = self.Ship_Number.text()
        dict["HP"] = self.Horsepower.text()
        dict["Rating"] = self.rating.text()
        dict["Hours"] = self.hours_day.text()
        return dict
        
    def letter_table(self):#generates the columns for the upper table "letter table" with totals
        self.user_arg = self.update_selections()
        # combine two argument into one column for the sea service letter table
        self.user_arg[r"Vessel Name/Number"] = self.user_arg["Ship Name"] + r"/" + self.user_arg["Ship Number"]
        self.user_arg["Nature of Voyage"] = self.user_arg["Nature"]
        
        #headers, 2 kinds, one for i= in p = port, and one for underway
        headers = [
        r"Vessel Name/Number","GRT","Propulsion", "HP", "Rating", 
        "Nature of Voyage", "Begin Date", "End Date", "Days Underway"
        ]
        ip_headers = [
        r"Vessel Name/Number","GRT","Propulsion", "HP", "Rating",
        "Begin Date", "End Date", "Creditable Days"
        ]
        
        #List comprehension/filter which turn dates into strings (date.today()).strftime("%d-%b-%Y")   to  dd-mm-yyyy 
        #also splits start days odd to finish days since: 1%2 = 1 which True and 2%2 = 0  which is false)
        end_days = [(day[1]-pd.Timedelta(days=1)).strftime("%d-%b-%Y") for odd,  day in enumerate(self.day_segment) if odd%2]
        begin_days = [day[1].strftime("%d-%b-%Y") for even,  day in enumerate(self.day_segment) if (even-1)%2]
         
        columns = {}
        num_rows = len(begin_days)
        #make headers keys, to a  the list so that: column = { header: [item1, item2, item3] , header2: [...], ...}
        #make the table in columns, add the last 3 outside the loop since they are already length of days
        
        head = headers
        
        if self.user_arg["Inport Letter"]:
            head = ip_headers
        print('using headers :', head)    
        for col in head[:-3]: #number of rows or the number of columns . Remove the last 3 items
            columns[col] = [ self.user_arg[col] ]*num_rows
            
        #now add the remaining 3 columns
        columns["Begin Date"] = begin_days # the "begin date " is the col header the list is the column
        columns["End Date"] = end_days 
        #the column title depends on the type of days
        if self.user_arg["Inport Letter"]:
            print("Inport time Letter Selected")
            columns["Creditable Days"] = self.u_w_days
        else: 
            columns["Days Underway"] = self.u_w_days
        self.headers = head
        num_cols = len(columns.keys())
        print('table columns: ',  columns.keys())
        self.table_cols =  columns
        self.table_num_rows = num_rows 
        self.table_num_cols = num_cols
    
    def letter_set_data(self):#feeds the columns to the gui Table Widget
        data = self.table_cols
        rows = self.table_num_rows+1
        cols = self.table_num_cols
        self.tableWidget.setRowCount(rows)
        self.tableWidget.setColumnCount(cols)
        self.tableWidget.setHorizontalHeaderLabels(self.table_cols.keys())
        #build the rows and columns
        for n, key in enumerate(data.keys()):#columns
            for m, item in enumerate(data[key]):#row by row down
                flags = Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable #for copy paste functionality
                newitem = QTableWidgetItem(item)
                newitem.setFlags(flags)
                self.tableWidget.setItem(m, n, newitem)

        #add total
        total = QTableWidgetItem(str(self.total_days))
        tot_label = QTableWidgetItem('Total:')
        self.tableWidget.setItem(rows-1, cols-2, tot_label)
        self.tableWidget.setItem(rows-1, cols-1,  total)
        self.tableWidget.itemChanged.connect(self.cell_changed)
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        self.tableWidget.show()
        
    def ms_word_dict(self): #repackages the table for MS Word formatting table
        self.word_rows = []

        for row in range( self.tableWidget.rowCount() ):
            ms_row = {}
            for col in range(self.tableWidget.columnCount()):
                # goes thru the table data starts with a row and attaches each col as a key to a dictionary
                # so we have key = {GRT: [column value for row GRT]} for each entry in this dictionary
                #each row of the ms table is a dictionary , confusing I know.
                key =self.tableWidget.horizontalHeaderItem(col).text()
                try:
                    item = self.tableWidget.item(row, col).text()
                except AttributeError: #in case of empty cell, None becomes ' '
                    item = " "
                print(item)
                ms_row[key] = item
                
                
            print(ms_row)
            self.word_rows.append(ms_row)    
        
    
    
    def set_up_file_download(self):#Finds the excel sheet  to read with data
        print("set up file download")
        #Various checks to see if a last name makes sense, if file is valid path etc
        if self.name == None:
            self.INFOBOX.setText("YOU NEED A LAST NAME TO SET UP TABLES")
            return
            
        elif self.name.isalpha():
            file_path = QFileDialog.getOpenFileName(self,'Open file', 
            self.program_directory,"Beguns's file's (*.xlsx)")[0]
            print(file_path)
            
        if file_path == None:
            print('no file path selected')
            return
        elif self.file_path == '':
            print('no file path selected')
            return
        elif not exists(file_path):
            self.INFOBOX.setText("INFO: Found Not File")
            return 
        else:
            self.file_path = file_path #store new file path
        return True
        
        
    def open_file(self):#helper function converts excell data to Pandas Data Frame
        self.d_frame = pd.read_excel(self.file_path,  header=17) #Uses the 17 row for heaer (keys of a dict)
        self.user_arg = self.update_selections()
       
        
#Here we set up rows, ordered <Name>, day type, ship day type, Date, and Day Number from top to bottom 
#When changing serached for name, we erase the previous table with a call to "recreate table".
    def data_prep(self):#admittedly the most complicated way to do this

        #switch Pandas data frame to a List object,, then remove the "\n" which excel added
        #columns holds all the names
        columns = [name.replace ('\n', ' ') for name in self.d_frame.columns.to_list() ]
        if not self.name in columns: # if last not found 
            print(self.name+" was not found in: ", columns)
            if  self.fullname.text():#try the full name
                self.user_arg = self.update_selections() #update
                name = self.user_arg["Full Name"]#use the full name to find data
                if name in columns:
                    print("found ", name)
                    self.INFOBOX.setText("Matched Full Name")
                else:#could not Last Name or Full Name in the file
                    self.recreate_table()
                    self.INFOBOX.setText("Check Last Name and Full Name ")
                    self.create_letter.setEnabled(False)
                    print('could not find last name either')
                    return
                    
            else:
                print('no last name there')
                self.recreate_table()
                self.create_letter.setEnabled(False)
                return  self.INFOBOX.setText("Name not found in file")#columns is a list of 5 elements which are columns headers from xlxs, 
        else:
            name = self.name
        
        #use the index since data frame has '\n'    
        self.index = next(i for i,  x in enumerate(columns) if x == name) 

        print(name)#here we'll make the row name in the TableView
        columns.insert(0, name)#add Name to the first slot on header list 
        self.columns = columns[:5] #chop  off all but first 5 column headers, 
        #format dates
        self.dates = [x.strftime("%d %B") for x in self.d_frame[self.columns[2]] ]  #we'll use the dates as columns header in new table
        print("have dates")
        # Rearanging list from[NAME, 'DN', 'Date', 'Location at end of day', "Ship's Status"] to [Name, shipstat, Loc, DN] -> 01234 to 0431
        try:
            self.columns = [self.columns[0], #name status [0]
                self.columns[4],#lship status ->[1]
                self.columns[3],#Location -> [2]
                self.columns[1], #DN -> [3]
                ]
        except KeyError as err:
            self.INFOBOX.setText(err.message + "name not found")
            print("name  not found")
            raise KeyError(key) from err
            self.INFOBOX.setText("INFO: Last Name Not Found")
        #now we use the headers to get dataframe rows and add them to make a list called "rows"
        #these will be the rows of the new table.
        prepped_rows = [] # container for full columns, will be come rows on table
        prepped_rows.append(self.d_frame.iloc[:, self.index]) #Person's column now a row, used the index value
        prepped_rows.append(self.d_frame[self.columns[1]]) #Ships stat
        prepped_rows.append(self.d_frame[self.columns[2]]) #Location
        #Day Number to strings not int
        prepped_rows.append( [str(x) for x in self.d_frame[ self.columns[3] ]]) 
        self.tableview_rows = prepped_rows
        
        
    def make_lcd(self):#this is for the LCD display values mostly
       
        lookup = self.d_frame.iloc[:, self.index]
        self.data = {
        "Not Aboard": len([x for x in lookup if x=="A"]), 
        "Training": len([x for x in lookup if x=="T"]), 
        "Sea Days": len([x for x in lookup if x==r"U/W"]), 
        "InPort" : len([x for x in lookup if x==r"I/P"]), 
        "Leave" : len([x for x in lookup if x=="L"]),
        "Dates" : self.d_frame["Date"],
        "Name's Column" : lookup,
        }  
        self.lcd_leave.display(self.data["Leave"])
        self.lcd_absent.display(self.data["Not Aboard"])
        self.lcd_inport.display(self.data["InPort"])
        self.lcd_seadays.display(self.data["Sea Days"])
        self.lcd_training.display(self.data["Training"])
       
        
    def create_tables(self): #calls a Table View widget, (Calender Table)
        #Set up the Table model and displays it
        print("creating Table View")
        #pass the prepped rows for the table View (not letter table). the columns(row lables now) and the 
        #row of dates of the years. 
        self.model = TableModel(self.tableview_rows, self.columns,  self.dates) 
        #present the model in the Table view with pretty colors
        self.tableView.setModel(self.model)#present the model in the Table view with pretty colors
        
    def sort_days(self): #sets up the day counts for the letter table
        segment = []
        self.user_arg = self.update_selections()
        counting = False #works like an on off switch for counting
        if self.data == None:
            return
        day = zip(self.data["Dates"], self.data["Name's Column"])
        #only counts U/W or I/P days
        iters = 0
        if self.user_arg["Inport Letter"]:
            day_type = self.data["InPort"] 
            s_key = r"I/P"
        else:
            day_type = self.data["Sea Days"]
            s_key = r"U/W"
        #we have every calander day zipped with their U/w or IP status
        while iters < day_type :
            s_date, status = next(day)# we go thru each pair
            
            if status == s_key: #------------#   IS  an U/W day or I/P depending
                if counting == False: #not counting yet, so start counting
                    segment.append(["Begin",  s_date])#records the start
                    counting = True #we are now counting
                    iters +=1
                    continue
                else:#already got the start date and already counting
                    iters +=1
                    continue #so we continue
            else:       #------------#   not an U/W day
                if counting == False: #wasn't counting beforepr
                    continue #continue not couting
                else: #we were counting and we have to stop
                    # record the day before as the last day of U/W; by subtracting 1.
                    segment.append(["end",  s_date ])
                    counting = False #we stop counting 
                    continue
                    
        if counting == True:
            self.INFOBOX.setText("U/W or I/P Accruing ")
        day_span = []
        self.total_days = 0
        #collect the day span by subtracting start date from finish date: end - start
        for element_num ,  begin2end in enumerate(segment):
            if element_num%2: #just the odd ones, 1, 3,5...
                #add back the day we subtracted for the math to (days = work end day minus begin day)
                delta = begin2end[1]- segment[element_num-1][1]
                self.total_days += int(delta.days)
                day_span.append(str(delta.days))
      
        self.day_segment = segment
        self.u_w_days = day_span 
        
    def eventFilter(self, source, event): #handles  CTRL - C copy from table to word
        if event.type() == QEvent.KeyPress:
            if event == QKeySequence.Copy:
                self.copySelection()
                return True
            elif event == QKeySequence.Paste:
                #self.pasteSelection() TO DO:
                #return True
                pass
        return super(Ui_SeaServiceMaster, self).eventFilter(source, event)
        
    #handles the pasting from anything copied from the Letter Table
    def copySelection(self):
        selected = self.tableWidget.selectedIndexes()
        col_head = self.headers 
        #col_dict = dict(zip( range(len(col_head)), col_head))
        row = [[] for x in range(self.tableWidget.rowCount())]
        col = [[] for x in range(self.tableWidget.columnCount())]

        headers = []
        for num,  item in enumerate( selected ): #can't select more rows than what the table holds
          
            if col_head[item.column()] not in headers:
                headers.append(col_head[item.column()])
            col[item.column()].append(item.data())
            row[item.row()].append(item.data())
        
        
        col = [ x for x in col if x != [] ]
        row = [ x for x in row if x!=[] ]
        #pass data to Pandas for manipulations
        df = pd.DataFrame(row,  columns = headers)
        #set up a tab seperated tabel with line terminator and remove the indexes 
        table = df.to_csv(sep='\t', line_terminator='\n',  index=False)
        clipboard = QGuiApplication.clipboard()
        #can be pasted into the templates now
        clipboard.setText(table)
 

#Creates the Table View Model by inheriting the QAbstracat Table Model
class TableModel(QAbstractTableModel):
    def __init__(self, data, row_labels, headers):
        super(TableModel, self).__init__()
        self._data = data
        self.row_labels =  row_labels
        self.headers = headers
        self.COLORS = ['#053061', '#2166ac', '#4393c3', 
            '#92c5de', '#d1e5f0', '#f7f7f7','#fddbc7',
            '#f4a582', '#d6604d', '#b2182b', '#67001f']
    
    def data(self,  index,  role):
        if role == Qt.DisplayRole:#assembles rows and columns of the table View
            show = self._data[index.row()][index.column()]
            if show == None:
                show = ""
            return show
            
        if role == Qt.BackgroundRole:
            value = self._data[index.row()][index.column()]
            #this is where the colors are added using a number , Default is white.
            if value == "I/P" :
                value =   7
            elif value == "U/W":
                value = 4
            elif value == "L":
                value= 6
            else:
                return QColor('white')

            return QColor(self.COLORS[value])
    
    def rowCount(self,  index):
        return len(self._data)    

    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        if role == Qt.DisplayRole:#this is where the lables go along the "y" axis
            if orientation == Qt.Horizontal:
                ##print(section)
                return self.headers[section]
                
            if orientation == Qt.Vertical:
                return self.row_labels[section]

    def columnCount(self,  index):
        return len(self._data[0])
    

##Finally runs the  application##
app = QApplication(sys.argv)
window = Ui_SeaServiceMaster()
window.show()
sys.exit(app.exec())

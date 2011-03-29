from PyQt4 import QtGui, QtCore, Qt

import config_if

COLUMN_IFS = 0
COLUMN_MITM = 1
COLUMN_OUT = 2

"""
TODO: Centering checkboxes requires a custom Item Delegate. We will avoid this
problem for now. Here are the relevant references:

http://developer.qt.nokia.com/faq/answer/how_can_i_align_the_checkboxes_in_a_view
http://lists.trolltech.com/qt-interest/2006-06/msg00476.html
http://stackoverflow.com/questions/4403704/qt-qtableview-alignment-of-checkbox-when-using-isusercheckable
http://stackoverflow.com/questions/1744348/embedding-a-control-in-a-qtableview

"""
class InterfacesGui(object):
    def __init__(self, interfaces_table):
        self.interfaces_table_view = interfaces_table
        self.interfaces_model = InterfacesTableModel()
        self.interfaces_table_view.setModel(self.interfaces_model)
        
        # Set column widths
        for column in self.interfaces_model.columns.keys():
            self.interfaces_table_view.setColumnWidth(column, 150)
        
    def resize_content_columns(self):
        self.interfaces_table_view.resizeColumnsToContents()      
        
class InterfacesTableModel(QtCore.QAbstractTableModel):
    def __init__(self, parent=None):
        super(InterfacesTableModel, self).__init__(parent)
    
        self.columns = {
                         0: "Interface Name",
                         1: "Perform MiTM",
                         2: "Outbound Interface"
                        }
                
        self.if_cfg = config_if.InterfacesConfigured()
        
        # Get interfaces, sort them, save them in if_cfg
        ni = config_if.NetworkInterfaces()
        ifs_list = ni.get_ifs().keys()
        ifs_list.sort()
        self.if_cfg.interfaces = ifs_list
            
        self.checked = True
    
    ## Required methods to subclass QAbstractTableModel    
    def rowCount(self, parent):
        return self.if_cfg.num_ifs()
    
    def flags(self, index):
        toggled_flags = QtCore.Qt.NoItemFlags
        toggled_flags |= QtCore.Qt.ItemIsEnabled

        if index.column() == COLUMN_MITM or index.column() == COLUMN_OUT:
            toggled_flags |= QtCore.Qt.ItemIsUserCheckable

        return toggled_flags
    
        #return 0
    
    def columnCount(self, parent):
        return len(self.columns)
    
    def setData(self, index, value, role):
        value_bool = value.toBool()
        column = index.column()
        row = index.row()
        
        if_name = self.if_cfg.get_if_for_idx(row)
        
        # Toggling MiTM
        if index.column() == COLUMN_MITM:
            if value_bool == False:
                self.if_cfg.set_mitm(if_name, False)
            else:
                self.if_cfg.set_mitm(if_name, True)
                
        # Toggling Outbound       
        if index.column() == COLUMN_OUT:
            if value_bool == False:
                self.if_cfg.set_outbound(if_name, False)
            else:
                self.if_cfg.set_outbound(if_name, True)
        
        
        top_left = self.createIndex(0, 0)
        bottom_right = self.createIndex(3, self.if_cfg.num_ifs())
        self.dataChanged.emit(top_left, bottom_right)
        
        return True
        
    def data(self, index, role):
        
        # Displaying Data
        if role == QtCore.Qt.DisplayRole:
            # Sanity check
            if index.row() < 0 or index.row() > self.if_cfg.num_ifs():
                return QtCore.QVariant()
            
            if index.column() == COLUMN_IFS:
                return self.if_cfg.get_if_for_idx(index.row())
            
            if index.column() == COLUMN_MITM:
                return QtCore.QVariant()

        # Editing Data (Not Needed)
        if role == QtCore.Qt.EditRole:
            if index.column() == COLUMN_MITM:
                pass
         
        # Align text   
        if role == QtCore.Qt.TextAlignmentRole:
            return QtCore.Qt.AlignCenter
         
        # Return internally managed checkbox state   
        if role == QtCore.Qt.CheckStateRole: 
            if_name = self.if_cfg.get_if_for_idx(index.row())
            
            if index.column() == COLUMN_MITM:
                if self.if_cfg.is_mitm(if_name):
                    return QtCore.Qt.Checked
                else:
                    return QtCore.Qt.Unchecked
            
            if index.column() == COLUMN_OUT:
                if self.if_cfg.is_outbound(if_name):
                    return QtCore.Qt.Checked
                else:
                    return QtCore.Qt.Unchecked
                    

        return QtCore.QVariant()
    ## Required methods to subclass QAbstractTableModel
    
    ## Optional methods for subclass of QAbstractTableModel 
    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.SizeHintRole:
            return QtCore.QSize(20, 20)
        
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                if section > -1 and section < len(self.columns):
                    return self.columns[section]
    ## Optional methods for subclass of QAbstractTableModel         
# -*- coding: utf-8 -*- 
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import wx
import wx.xrc
import dialog

class Editor ( wx.Frame ):
	
	def __init__( self, parent, note_name ):
		self.notename = note_name
		
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = note_name, pos = wx.DefaultPosition, size = wx.Size( 340,429 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.note = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		self.note.SetFont( wx.Font( 9, 73, 90, 90, False, "Comic Sans MS" ) )
		self.note.SetBackgroundColour( wx.Colour( 213, 213, 255 ) )
		self.note.SetMinSize( wx.Size( -1,5000 ) )
		with open ('.\Notes\kek'[0:8]+note_name+'.txt', 'r') as note_op:
			k = note_op.read()
			self.note.SetValue(unicode(k.encode('utf-8')))
		
		bSizer2.Add( self.note, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer2 )
		self.Layout()
		self.statusbar = self.CreateStatusBar( 2, wx.ST_SIZEGRIP, wx.ID_ANY )
		self.file_menu = wx.MenuBar( 0 )
		self.filemenu = wx.Menu()
		self.save_btn = wx.MenuItem( self.filemenu, wx.ID_ANY, u"Save"+ u"\t" + u"Ctrl+S", wx.EmptyString, wx.ITEM_NORMAL )
		self.filemenu.AppendItem( self.save_btn )
		
		self.file_menu.Append( self.filemenu, u"File" ) 
		
		self.SetMenuBar( self.file_menu )
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.save_question )
		self.Bind( wx.EVT_KEY_DOWN, self.check_save )
		self.note.Bind( wx.EVT_TEXT, self.statsrefresh )
		self.Bind( wx.EVT_MENU, self.save_note, id = self.save_btn.GetId() )
		
		self.statusbar.SetStatusText('Saved')
		
		self.Show(True)
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	
	def save_question( self, event ):
		a = self.statusbar.GetStatusText()
		if a != 'Saved':
			ret  = wx.MessageBox('Save file?', 'Question', 
			wx.YES_NO | wx.NO_DEFAULT, self)
			
			if ret == wx.YES:
				with open ('.\Notes\kek'[0:8]+self.notename+'.txt', 'w') as notesave:
					notesave.write(self.note.GetValue().encode('utf-8'))
				self.Destroy() 
			if ret == wx.NO:
				self.Destroy()
			
		else: self.Destroy()
		
	
	def check_save( self, event ):
		event.Skip()
	
	def statsrefresh( self, event ):
		self.statusbar.SetStatusText(str(len(self.note.GetValue())) + ' symbols'+ ' | ' + str(len(self.note.GetValue().replace(' ', '')))+ ' symbols')
	
	def save_note( self, event ):
		with open ('.\Notes\kek'[0:8]+self.notename+'.txt', 'w') as notesave:
			notesave.write(self.note.GetValue().encode('utf-8'))
		self.statusbar.SetStatusText('Saved')
		
	


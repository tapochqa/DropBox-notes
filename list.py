# -*- coding: utf-8 -*- 


import wx
import wx.xrc
import os
import main
import glob
import editor

class Notelist ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Note List", pos = wx.DefaultPosition, size = wx.Size( 248,428 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )
		self.SetBackgroundColour( wx.Colour( 255, 193, 217 ) )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		
		def choice():
			listChoices = []
			all_files = glob.glob('.\Notes\*.txt')
			for every_file in all_files:
				listChoices.append (every_file.replace('.\Notes\kek'[0:8], '').replace('.txt', ''))
			return listChoices
		
		note_listChoices = choice()
		
		self.note_list = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, note_listChoices, wx.LB_ALWAYS_SB )
		self.note_list.SetFont( wx.Font( 9, 73, 90, 90, False, "Comic Sans MS" ) )
		self.note_list.SetBackgroundColour( wx.Colour( 251, 230, 255 ) )
		self.note_list.SetMinSize( wx.Size( -1,300 ) )
		
		bSizer1.Add( self.note_list, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.note_name = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.note_name.SetMaxLength( 50 ) 
		self.note_name.SetFont( wx.Font( 9, 73, 90, 90, False, "Comic Sans MS" ) )
		self.note_name.SetToolTipString( u"New note name" )
		
		bSizer1.Add( self.note_name, 0, wx.ALL|wx.EXPAND, 5 )
		
		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )
		
		
		bSizer1.Add( gSizer1, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_menubar2 = wx.MenuBar( 0 )
		self.note_menu = wx.Menu()
		self.mnew = wx.MenuItem( self.note_menu, wx.ID_ANY, u"New note"+ u"\t" + u"Ctrl+N", wx.EmptyString, wx.ITEM_NORMAL )
		self.note_menu.AppendItem( self.mnew )
		
		self.mdel = wx.MenuItem( self.note_menu, wx.ID_ANY, u"Delete this note"+ u"\t" + u"Ctrl+D", wx.EmptyString, wx.ITEM_NORMAL )
		self.note_menu.AppendItem( self.mdel )
		
		self.m_menubar2.Append( self.note_menu, u"Note" ) 
		
		self.cloud_menu = wx.Menu()
		self.mupload = wx.MenuItem( self.cloud_menu, wx.ID_ANY, u"Upload"+ u"\t" + u"Ctrl+U", wx.EmptyString, wx.ITEM_NORMAL )
		self.cloud_menu.AppendItem( self.mupload )
		
		self.mdownload = wx.MenuItem( self.cloud_menu, wx.ID_ANY, u"Download"+ u"\t" + u"Ctrl+L", wx.EmptyString, wx.ITEM_NORMAL )
		self.cloud_menu.AppendItem( self.mdownload )
		
		self.m_menubar2.Append( self.cloud_menu, u"Cloud" ) 
		
		self.SetMenuBar( self.m_menubar2 )
		
		self.list_bar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_KEY_DOWN, self.check_key )
		self.note_list.Bind( wx.EVT_KEY_DOWN, self.check_enter )
		self.note_list.Bind( wx.EVT_LISTBOX_DCLICK, self.open_note )
		self.Bind( wx.EVT_MENU, self.new_note, id = self.mnew.GetId() )
		self.Bind( wx.EVT_MENU, self.delete_note, id = self.mdel.GetId() )
		self.Bind( wx.EVT_MENU, self.upload, id = self.mupload.GetId() )
		self.Bind( wx.EVT_MENU, self.download, id = self.mdownload.GetId() )
		
		self.note_name.Bind( wx.EVT_TEXT_ENTER, self.new_note )
		self.Show(True)
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class\
	
		
	def check_key( self, event ):
		event.Skip()
	
	def check_enter( self, e ):
		key = e.GetKeyCode()

		if key == wx.WXK_RETURN:
			a = self.note_list.GetString(self.note_list.GetSelection())
			editor.Editor(None, note_name= a)
	
	def open_note( self, event ):
		a = self.note_list.GetString(self.note_list.GetSelection())
		editor.Editor(None, note_name= a)
	
	def new_note( self, event ):
		main.create_new_note(self.note_name.GetValue())
		self.note_list.Append(self.note_name.GetValue())
		self.note_name.SetValue('')
		
	def delete_note( self, event ):
		k = self.note_list.GetString(self.note_list.GetSelection())
		path = '.\Notes\kek'[0:8]+k+'.txt'
		os.remove(path)
		self.note_list.Delete(self.note_list.GetSelection())
	
	def upload( self, event ):
		self.list_bar.SetStatusText('Uploading...')
		try:
			main.upload()
		except Exception:
			self.list_bar.SetStatusText('Failed')
		else:
			self.list_bar.SetStatusText('Uploaded')
	
	def download( self, event ):
		self.note_list.Clear()
		self.list_bar.SetStatusText('Downloading')
		try:
			
			main.download()
			for note in glob.glob('.\Notes\*.txt'):
				self.note_list.Append(note.replace('.\Notes\kek'[0:8], '').replace('.txt', ''))
		except Exception:
			self.list_bar.SetStatusText('Failed')
		else:
			self.list_bar.SetStatusText('Downloaded')
list = wx.App()
Notelist(None)
list.MainLoop()
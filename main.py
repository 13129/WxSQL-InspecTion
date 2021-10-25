# -*- coding: utf-8 -*-
import wx
import wx.xrc
import wx.dataview
import wx.lib.mixins.listctrl as listmix
from wx.core import MenuBar, Size, ToolBar
from wx.lib.agw import ultimatelistctrl as ULC
from wx.lib.embeddedimage import PyEmbeddedImage
# import img



class MyFrame (wx.Frame):
    t_col1 =['1','2','3']
    t_col4 = ['1', '1', '3', '5', '5', '1', '2']
    colhead = ["选择", "任务名称", "运行状态", "任务类型", "添加任务", "修改时间", "操作"]
    colwidth = [50, 200, 60, 100, 140, 140, 140]
    task_category_list = ['数据库']

    


    def __init__(self, parent,title):
        super(MyFrame,self).__init__( parent, title=title,style = wx.DEFAULT_FRAME_STYLE)
        self.InitUI()

    def InitUI(self):
        self.initUIMenuBar()  # 初始化 菜单栏
        self.initUIToolsBar()
        self.initUIStatusBar()  # 初始化 状态栏
        self.initUIMainWindow()  # 构建 窗口面板
        self.creatList()
        self.adjustmentWin()  # 调整 窗口框体参数

    def initUIMenuBar(self):
        self.m_menubar1 = wx.MenuBar(0)
        self.m_menu1 = wx.Menu()
        self.m_menubar1.Append(self.m_menu1, u"MyMenu")
        self.SetMenuBar(self.m_menubar1)

        # pass
    def initUIToolsBar(self):
        self.toolbar = self.CreateToolBar(wx.TB_HORIZONTAL, wx.ID_ANY)
        self.toolbar.Realize()
        # pass
    def initUIStatusBar(self):
        self.statusBar = self.CreateStatusBar(1,id=-1)

       
    def initUIMainWindow(self):
        self.panel = wx.Panel(self, -1, size = (900, 600))
        self.panel.SetBackgroundColour('White')

        self.listBox = wx.BoxSizer()  # 定义横向列表
        self.list_results = ULC.UltimateListCtrl(self.panel, agwStyle = ULC.ULC_REPORT
                                                                        # |ULC.ULC_NO_HIGHLIGHT
                                                                        |ULC.ULC_BORDER_SELECT
                                                                    |ULC.ULC_STICKY_HIGHLIGHT
                                                                   |ULC.ULC_HAS_VARIABLE_ROW_HEIGHT
                                                                   |ULC.ULC_HOT_TRACKING)
                                                                
        #设定表头
        for x in range(0, len(self.colhead)):
                self.list_results.InsertColumn(x, self.colhead[x], width=self.colwidth[x],format=ULC.ULC_FORMAT_CENTRE)
        self.listBox.Add(self.list_results, 1, wx.EXPAND | wx.CENTER, 5)

        # #新建按钮区域
        # addTaskSizer = wx.BoxSizer(wx.HORIZONTAL)

        # bmp4=wx.Image('./add_task.png',wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        # self.addTaskButton = wx.BitmapButton(self.panel, wx.ID_ANY,bmp4, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW)
        # addTaskSizer.Add(self.addTaskButton, 0, wx.ALL, 5)
        # #运行结果 operaResult
        # operaResultSizer = wx.BoxSizer(wx.VERTICAL)
        # self.operaResultdataViewList = wx.dataview.DataViewListCtrl(self.panel, wx.ID_ANY, wx.DefaultPosition,(-1,-1), 0)
        # operaResultSizer.Add(self.operaResultdataViewList, 0, wx.ALL, 5)

        #最外层verticalSizer
        verticalSizer = wx.BoxSizer(wx.VERTICAL)
        verticalSizer.Add(self.listBox,1,wx.EXPAND,5)
        # verticalSizer.Add(addTaskSizer, 1, wx.EXPAND, 5)
        # verticalSizer.Add(operaResultSizer, 1, wx.EXPAND, 5)

        self.panel.SetSizer(verticalSizer)
        self.panel.Layout()
        self.panel.Centre(wx.BOTH)

    def creatList(self):
        for x in range(0, len(self.t_col1)):
            self.list_results.InsertStringItem(x, '')
            cBox = wx.CheckBox(self.list_results,-1)
            self.task_category_choice=wx.Choice(self.list_results,-1,size=(90,30),choices=self.task_category_list)
            self.task_category_choice.SetSelection(0)

            bmp0=wx.Image('./add.png',wx.BITMAP_TYPE_PNG).ConvertToBitmap()
            bmp1=wx.Image('./start.png',wx.BITMAP_TYPE_PNG).ConvertToBitmap()
            bmp2=wx.Image('./pause.png',wx.BITMAP_TYPE_PNG).ConvertToBitmap()
            self.addButton = wx.BitmapButton(self.list_results, wx.ID_ANY, bmp0,size=(30,30))
            self.startButton = wx.BitmapButton(self.list_results, wx.ID_ANY, bmp1,size=(30,30))
            self.pauseButton = wx.BitmapButton(self.list_results,wx.ID_ANY,bmp2,size=(30,30))       
            self.list_results.SetItemWindow(x, 0, cBox)
            self.list_results.SetStringItem(x, 1, '测试任务')
            self.list_results.SetStringItem(x, 2, '正在进行')
            self.list_results.SetItemWindow(x, 3, self.task_category_choice)
            self.list_results.SetItemWindow(x, 4, self.addButton)
            self.list_results.SetStringItem(x, 5, '2021-07-12 22:00:22')
            self.list_results.SetItemWindow(x, 6, self.startButton,True)

            wx
            # self.list_results.SetItemWindow(x, 6, self.pauseButton)

    def adjustmentWin(self):
        self.SetSize((900, 600))
        self.Center()
        self.Show()


if __name__ == '__main__':
    ex = wx.App()
    MyFrame(None, 'WXSQL-InSpecTion')
    ex.MainLoop()

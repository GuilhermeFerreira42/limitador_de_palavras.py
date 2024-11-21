import wx
import wx.stc

class LimitadorPalavrasApp(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="Limitador de Palavras", size=(600, 650))

        # Criar painel principal
        panel = wx.Panel(self)
        
        # Criar sizer principal
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        
        # Área de quantidade de palavras
        palavras_sizer = wx.BoxSizer(wx.HORIZONTAL)
        label_remover = wx.StaticText(panel, label="Quantidade de palavras:")
        self.entry_remover = wx.TextCtrl(panel, size=(200, -1))
        palavras_sizer.Add(label_remover, 0, wx.ALL | wx.CENTER, 5)
        palavras_sizer.Add(self.entry_remover, 1, wx.ALL | wx.EXPAND, 5)
        
        # Área de texto de entrada
        texto_label = wx.StaticText(panel, label="Insira o texto:")
        self.entry_texto = wx.stc.StyledTextCtrl(panel, size=(580, 150))
        self.entry_texto.SetWrapMode(wx.stc.STC_WRAP_WORD)
        self.entry_texto.SetMarginWidth(1, 0)

        # Área de texto de resultado
        resultado_label = wx.StaticText(panel, label="Texto processado:")
        self.entry_resultado = wx.stc.StyledTextCtrl(panel, size=(580, 150))
        self.entry_resultado.SetWrapMode(wx.stc.STC_WRAP_WORD)
        self.entry_resultado.SetMarginWidth(1, 0)
                
        # Botões principais
        botoes_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.btn_processar = wx.Button(panel, label="Processar")
        botoes_sizer.Add(self.btn_processar, 0, wx.ALL, 5)
        
        # Labels de contagem
        self.label_contagem_texto = wx.StaticText(panel, label="Palavras: 0")
        self.label_contagem_resultado = wx.StaticText(panel, label="Palavras: 0")
        
        # Adicionar elementos ao sizer principal
        main_sizer.Add(palavras_sizer, 0, wx.EXPAND | wx.ALL, 5)
        main_sizer.Add(texto_label, 0, wx.ALL, 5)
        main_sizer.Add(self.entry_texto, 1, wx.EXPAND | wx.ALL, 5)
        main_sizer.Add(self.label_contagem_texto, 0, wx.ALL, 5)
        main_sizer.Add(botoes_sizer, 0, wx.CENTER | wx.ALL, 5)
        main_sizer.Add(resultado_label, 0, wx.ALL, 5)
        main_sizer.Add(self.entry_resultado, 1, wx.EXPAND | wx.ALL, 5)
        main_sizer.Add(self.label_contagem_resultado, 0, wx.ALL, 5)
        
        # Configurar o sizer
        panel.SetSizer(main_sizer)
        
        # Centralizar a janela
        self.Center()
        
        # Bind de eventos
        self.entry_texto.Bind(wx.stc.EVT_STC_CHANGE, self.atualizar_contagem_texto)
        self.entry_resultado.Bind(wx.stc.EVT_STC_CHANGE, self.atualizar_contagem_resultado)
        self.btn_processar.Bind(wx.EVT_BUTTON, self.processar_texto)
        
        # Mostrar a janela
        self.Show()

    def atualizar_contagem_texto(self, event):
        texto = self.entry_texto.GetText()
        self.label_contagem_texto.SetLabel(f"Palavras: {len(texto.split())}")
        event.Skip()

    def atualizar_contagem_resultado(self, event):
        texto = self.entry_resultado.GetText()
        self.label_contagem_resultado.SetLabel(f"Palavras: {len(texto.split())}")
        event.Skip()

    def processar_texto(self, event):
        try:
            limite_palavras = int(self.entry_remover.GetValue())
            texto = self.entry_texto.GetText().strip()
            
            palavras = texto.split()
            palavras_processadas = ' '.join(palavras[:limite_palavras])
            
            resultado_final = palavras_processadas
            self.entry_resultado.SetText(resultado_final)
        except ValueError:
            wx.MessageBox("Por favor, insira um número válido.", "Erro",
                         wx.OK | wx.ICON_ERROR)

if __name__ == "__main__":
    app = wx.App(False)
    frame = LimitadorPalavrasApp()
    app.MainLoop()
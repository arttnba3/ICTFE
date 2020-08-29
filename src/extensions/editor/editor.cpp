//
// Created by reverier on 2020/7/29.
//

#include "editor.h"
#include "ui_editor.h"
#include "editorSettingPage.h"
#include <KTextEditor/ConfigInterface>
#include <KTextEditor/ConfigPage>
// #include <QMenu>

Editor::Editor(QWidget *parent, QFlags<Qt::WindowType> flags) :
        ISAEPluginWidget(parent, flags), ui(new Ui::Editor) {
    ui->setupUi(this);
    this->setSettingWindow(new EditorSettingPage(this));
    this->m_settings = new QSettings();
    this->m_name = "Editor";
    this->m_icon = ":/plugins/editor.svg";
    int n = ui->editorStack->count();
    for (auto i = n - 1; i >= 0; i--) {
        ui->editorStack->removeWidget(ui->editorStack->widget(i));
    }
    this->m_hexEditor = new HexEditor(this);
    KTextEditor::Editor *editor = KTextEditor::Editor::instance();
    KTextEditor::Document *doc = editor->createDocument(this);
    auto *l = new QWidget();
    this->m_textEditor = doc->createView(l);
    auto iface = qobject_cast<KTextEditor::ConfigInterface *>(this->m_textEditor);
    iface->setConfigValue("background-color", QColor(32, 36, 40));
    iface->setConfigValue("icon-border-color", QColor(33, 37, 41));
    ui->editorStack->addWidget(this->m_textEditor);
    ui->editorStack->addWidget(this->m_hexEditor);
//    QMenu* menu = new QMenu();
//    menu->addMenu("hello");
//    menu->addAction("test");
//    this->m_textEditor->setContextMenu(menu);
    // this->m_hexEditor->setStyleSheet("background-color: transparent;");
    this->m_hexEditor->setAcceptDrops(true);
    ui->modeChooser->addItem("文本模式");
    ui->modeChooser->addItem("Hex模式");
    ui->editorStack->setCurrentWidget(this->m_textEditor);
    auto* page = (EditorSettingPage*)(this->m_settingWindow);
    QStringList list = {"外观", "编辑器颜色", "编辑选项", "文件"};
    for (int i = 0; i < editor->configPages(); i++) {
        page->addPage(editor->configPage(i, page), list[i]);
    }
    QObject::connect(ui->modeChooser, SIGNAL(currentTextChanged(const QString &)), SLOT(setMode(const QString &)));
}

void Editor::setMode(const QString &mode) {
    if (mode == "文本模式") ui->editorStack->setCurrentWidget(this->m_textEditor);
    else ui->editorStack->setCurrentWidget(this->m_hexEditor);
}

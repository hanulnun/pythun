import sys
from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *
from PyQt5.QtGui import *
from pandas import Series, DataFrame


class Kiwoom_sample(QMainWindow):
    def __init__(self):
        super().__init__()

        # Kiwoom Login
        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        # self.kiwoom.dynamicCall("CommConnect()")

        # OpenAPI+ Event
        self.kiwoom.OnEventConnect.connect(self.login_event_connect)
        self.kiwoom.OnReceiveTrData.connect(self.receive_trdata)

        btn_login = QPushButton("Login", self)
        btn_login.move(10, 20)
        btn_login.clicked.connect(self.login_btn_click)

        self.setWindowTitle("Kiwoom sample")
        self.setGeometry(300, 300, 380, 350)

        label = QLabel('종목코드')
        label.move(20, 20)

        self.code_edit = QLineEdit(self)
        self.code_edit.move(150, 20)
        self.code_edit.setText("039490")

        btn_search_code = QPushButton("조회", self)
        btn_search_code.move(260, 20)
        btn_search_code.clicked.connect(self.search_btn_click)

        self.text_edit = QTextEdit(self)
        self.text_edit.setGeometry(10, 160, 350, 120)
        # self.text_edit.setEnabled(False)

        btn_get_account = QPushButton("계좌조회", self)
        btn_get_account.move(10, 60)
        btn_get_account.clicked.connect(self.get_account)

        btn_get_all_list = QPushButton("종목가져오기", self)
        btn_get_all_list.move(120, 60)
        btn_get_all_list.clicked.connect(self.get_list)

    def get_list(self):
        ret = self.kiwoom.dynamicCall("GetCodeListByMarket(QString)", ["0"])
        kospi_code_list = ret.split(';')
        kospi_code_name_list = []

        for kospi_code in kospi_code_list:
            name = self.kiwoom.dynamicCall("GetMasterCodeName(QString)", [kospi_code])
            self.text_edit.append(kospi_code + " : " + name)

    def get_account(self):
        account_num = self.kiwoom.dynamicCall("GetLoginInfo(QString)", ["ACCNO"])
        self.text_edit.append("계좌번호 : " + account_num)

    def login_btn_click(self):
        self.kiwoom.dynamicCall("CommConnect()")

    def login_event_connect(self, err_code):
        if err_code == 0:
            self.text_edit.setText("Login 성공")
        else:
            self.text_edit.setText("Login 실패" + err_code)

    def search_btn_click(self):
        search_code = self.code_edit.text()
        self.text_edit.setText("종목코드 : " + search_code)
        # 변수 설정
        self.kiwoom.dynamicCall("SetInputValue(QString, QString)", "종목코드", search_code)
        # API CALL
        self.kiwoom.dynamicCall("CommRqData(QString, QString, int, QString)", "opt10001_req", "opt10001", 0, "0101")

    def receive_trdata(self, screen_no, rqname, trcode, recordname, prev_next, data_len, err_code, msg1, msg2):
        if rqname == "opt10001_req":
            name = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "종목명")
            volume = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "거래량")
            결산월 = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname,
                                             0, "결산월")
            영업이익 = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname,
                                          0, "영업이익")

            self.text_edit.append("종목명: " + name.strip())
            self.text_edit.append("거래량: " + volume.strip())
            self.text_edit.append("결산월: " + 결산월.strip())
            self.text_edit.append("영업이익: " + 영업이익.strip())
            self.text_edit.append("근재야 오늘도 수고했다!")


def pandas_test():
    me = Series([10, 20, 30], index=['kt', 'naver', 'kakao'])
    you = Series([20, 30, 10], index=['kakao', 'naver', 'kt'])
    we = me + you
    print(we)


def data_frame_test():
    row_data = {'col1': [1, 2, 3, 4],
                'col2': [10, 20, 30, 40],
                'col3': [100, 200, 300, 400]}
    data = DataFrame(row_data)
    print(row_data)
    print(data)


if __name__ == "__main__":
    row_data = {'col1': [1, 2, 3, 4],
                'col2': [10, 20, 30, 40],
                'col3': [100, 200, 300, 400]}
    data = DataFrame(row_data)
    print(row_data)
    print(data)
    # data_frame_test()
    # pandas_test()
    # app = QApplication(sys.argv)
    # Kiwoom_sample = Kiwoom_sample()
    # Kiwoom_sample.show()
    # app.exec_()

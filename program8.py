def main():
    app = QApplication(sys.argv)
    
    w = Simple_drawing_winndow()
    w.show()

    return app.exec_()
    if __name__=="__main__":
        sys.exit(main())

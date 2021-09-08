class LanguageFormat(object):
    Ukraine = 0
    USA = 1


class Report(object):
    def __init__(self, format_):
        self.title_ukr = 'Привіт!'
        self.title_usa = 'Hello!'
        self.format_ = format_


class Handler(object):
    def __init__(self):
        self.nextHandler = None

    def handle(self, req):
        self.nextHandler.handle(req)


class UkraineHandler(Handler):
    def handle(self, req):
        if req.format_ == LanguageFormat.Ukraine:
            print(f'Ukraine: {req.title_ukr}')
        else:
            super().handle(req)


class USAHandler(Handler):
    def handle(self, req):
        if req.format_ == LanguageFormat.USA:
            print(f'USA: {req.title_usa}')
        else:
            super().handle(req)


class ErrorHandler(Handler):
    def handle(self, req):
        print("Invalid request")


if __name__ == '__main__':
    report = Report(LanguageFormat.Ukraine)

    ukr_handler = UkraineHandler()
    usa_handler = USAHandler()

    ukr_handler.nextHandler = usa_handler
    usa_handler.nextHandler = ErrorHandler()

    ukr_handler.handle(report)

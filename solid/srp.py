# Single Responsibility Principle (SRP) – każda klasa ma jedną odpowiedzialność

class ReportGenerator:
    def generate(self, data):
        return f"Report: {data}"

class ReportPrinter:
    def print(self, report):
        print(report)
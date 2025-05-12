class ReportGenerator:
    def __init__(self, title):
        self.title = title

    def generate_report(self, expenses):
        report = f"{self.title}:\n"
        for expense in expenses:
            report += f"{expense['amount']} - {expense['category']} - {expense['date']}\n"
        return report

class DailyReportGenerator(ReportGenerator):
    def __init__(self):
        super().__init__("Отчёт на сегодня")

class WeeklyReportGenerator(ReportGenerator):
    def __init__(self):
        super().__init__("Еженедельный отчёт")
    
class MonthlyReportGenerator(ReportGenerator):
    def __init__(self):
        super().__init__("Месячный отчёт")

class ReportGeneratorFactory:
    def get_report_generator(self, report_type):
        if report_type == 'daily':
            return DailyReportGenerator()
        elif report_type == 'weekly':
            return WeeklyReportGenerator()
        elif report_type == 'monthly': 
            return MonthlyReportGenerator()
        else:
            return None
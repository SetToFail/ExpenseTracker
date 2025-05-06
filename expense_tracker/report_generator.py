# expense_tracker/report_generator.py

class ReportGenerator:
    def generate_report(self, expenses):
        report = ""
        for expense in expenses:
            report += f"{expense[0]} - {expense[1]} - {expense[3]}\n"  # Доступ к элементам по индексу
        return report

class DailyReportGenerator(ReportGenerator):
    def generate_report(self, expenses):
        report = "Отчёт на сегодня:\n"
        for expense in expenses:
            report += f"{expense[0]} - {expense[1]} - {expense[3]}\n"  # Доступ к элементам по индексу
        return report

class WeeklyReportGenerator(ReportGenerator):
    def generate_report(self, expenses):
        report = "Еженедельный очёт:\n"
        for expense in expenses:
            report += f"{expense[0]} - {expense[1]} - {expense[3]}\n"  # Доступ к элементам по индексу
        return report
    
class MonthlyReportGenerator(ReportGenerator):
    def generate_report(self, expenses):
        report = "Месячный отчёт:\n"
        for expense in expenses:
            report += f"{expense[0]} - {expense[1]} - {expense[3]}\n"
        return report


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
# Builder (Строитель)
# используется для создания тестовых данных (сущности: users, products, orders)

class Laborer:
    def __init__(self, name: str, email: str, role: str, is_active: bool, department: str):
        self.name = name
        self.email = email
        self.role = role
        self.is_active = is_active
        self.department = department


class LaborerBuilder:
    # конструктор используется для генерации дефолтных значений
    def __init__(self, name: str, email: str, role: str, is_active: bool, department: str):
        self.name = 'Vadim'
        self.email = 'vadim_zviagintsev@gmail.com'
        self.role = 'QA Automation'
        self.is_active = True
        self.department = 'QA'


    def set_name(self, new_name: str):
        self.name = new_name
        return self


    def set_email(self, new_email: str):
        self.email = new_email
        return self


    def set_role(self, new_role: str):
        self.role = new_role
        return self


    def deactivate(self):
        self.is_active = False
        return self


    def set_department(self, new_department: str):
        self.department = new_department
        return self


    def build(self) -> Laborer:
        return Laborer(self.name, self.email, self.role, self.is_active, self.department)



# Применение в автотесте

laborer_payload = (LaborerBuilder()
                   .set_name('Greg')
                   .set_email('greg_dev@google.com')
                   .set_role('developer')
                   .set_department('Frontend')
                   .build())
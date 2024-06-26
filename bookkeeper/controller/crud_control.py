from os import path


from bookkeeper.models.entities import db
import bookkeeper.controller.query_helper as qh


class CrudController:
    def __init__(self):
        try:
            db.bind(provider='sqlite', filename='../../config/database.sqlite', create_db=True)
            db.generate_mapping(create_tables=True)
        except Exception as e:
            print(e)

    def create(self, entity, params = any):
        if entity == 'Budget':
            qh.add_budget(monthly=params['monthly'], weekly=params['weekly'],
                          daily=params['daily'])
            return

        raise NotImplementedError(f'Добавление для сущности {entity} не реализовано!')

    def read(self, entity, params = any):
        if entity == 'Budget':
            return qh.get_budget()
        if entity == 'Category':
            return qh.get_category()

        raise NotImplementedError(f'Чтение для сущности {entity} не реализовано!')

    def update(self, entity, params = any):
        if entity == 'Budget':  # For Budget, update is the same as create
            qh.add_budget(monthly=params['monthly'], weekly=params['weekly'],
                          daily=params['daily'])
            return

        raise NotImplementedError(f'Изменение для сущности {entity} не реализовано!')

    def delete(self, entity):
        raise NotImplementedError(f'Удаление для сущности {entity} не реализовано!')
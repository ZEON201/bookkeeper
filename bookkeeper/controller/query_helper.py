
from pony.orm import *
from bookkeeper.models.entities import Budget, Category


@db_session
def add_budget(monthly, weekly, daily):
    try:
        Budget(monthly=monthly, weekly=weekly, daily=daily)
    except Exception as e:
        print(e)


@db_session
def get_budget():
    try:
        q = select(b for b in Budget).order_by(lambda: desc(b.id)).limit(1)
        budget = q.to_list()[0]
        return tuple([budget.monthly, budget.weekly, budget.daily])
    except Exception as e:
        print(e)

@db_session
def get_category():
    try:
        q = select((c.parent.name, c.name) for c in Category if c.parent is not None)
        cats = list(q)
        return tuple(" > ".join(cat) for cat in cats)
    except Exception as e:
        print(e)
@db_session
def add_category(name, locations):
    loc_entities = []
    for l in locations:
        try:
            cat = Category[l]
        except db_session.core.ObjectNotFound:
            cat = Category(name=l)
        else:
            loc_entities.append(cat)
    cat = Category(name=name, locations=loc_entities)
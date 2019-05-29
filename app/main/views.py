from app.models import Model
from . import main


@main.route('/')
def index():
    model = Model.query.filter_by(id=1).first()
    return 'ok'

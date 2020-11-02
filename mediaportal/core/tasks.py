import importlib
from celery.decorators import task


@task(name='increase_content_counter_task')
def increase_counter(id_, class_name):
    module = importlib.import_module('core.models')
    class_ = getattr(module, class_name)
    content = class_.objects.select_for_update().get(pk=id_)
    content.increase_counter()

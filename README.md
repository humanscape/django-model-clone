# django-model-clone
duplication of django model object

## Installation
```sh
pip install django-model-clone
```

## Usage

#### Using the CloneMixin

```
from django.db import models
from django.utils.translation import gettext_lazy as _
from model_clone import CloneMixin

class Example(models.Model, CloneMixin):
    title = models.CharField(max_length=200)
    children =  models.ManyToManyField('Child')

    _clone_many_to_many_related_fields=['children']


class Child(models.Model, CloneMixin): 
    name = models.CharField(max_length=255)
```

#### Duplicating a model instance

```py
In [1]: test_obj = Example.objects.create(title='test obj')

In [2]: test_obj.pk
Out[2]: 1

In [4]: test_obj.children.create(name='children1')

In [4]: test_obj.children.create(name='children2')

In [5]: test_obj.children.all()
Out[5]: <QuerySet [<Child: children1>, <Child: children2>]>

In [6]: cloned_test_obj = test_obj.clone()

In [7]: cloned_test_obj.pk
Out[7]: 2

In [8]: cloned_test_obj.title
Out[8]: 'test obj'

In [9]: cloned_test_obj.children.all()
Out[9]: <QuerySet [<Child: children1>, <Child: children2>]>
```
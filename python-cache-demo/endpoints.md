### Available endpoints per service

#### Infra-service

- [GET] /devices \
  Get all registered devices.
- [POST] /devices \
  Register new device.
  Params:
  - owner (int): id of the owner
  - model (int/str): id or name of the model
- [GET] /models \
  Get all models.
- [POST] /models \
   Add new model.
  Params:
  - category (int): id of the category
  - name (str): name of the model
  - energy_cons (float): energy consumption of the model
- [GET] /categories \
  Get all categories.
- [POST] /categories \
   Add new category.
  Params:
  - name (str): name of the category
- [GET] /getConsumption/models/\<string:model_name\> \
   Get calculated energy consumption for all devices from provided model.
  Params:
  - model_name (str): name of the model

#### Geo-service

- [GET] /positions/\<int:device_id\> \
  Get position of given device.
  Params:
  - device_id (int): id of the device
- [POST] /positions \
  Add new device's position.
  Params:
  - device_id (int): id of the existing device
  - pos_x (float): position x of the device
  - pos_y (float): position y of the device

#### Stats-service

- [GET] /metrics \
  Get all available metrics.

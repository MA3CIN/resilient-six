## Available endpoints per service

### Infra-service

- [GET] /devices \
  Get all registered devices. \
  Returns:
  - TODO
- [GET] /devices/\<id:owner_id> \
   Get all registered devices belonging to particular user. \
   Params:
  - owner_id (int): id of the owner
- [POST] /devices \
  Register new device. \
  Params:

  - owner (int): id of the owner
  - model (int/str): id or name of the model \
    Request:

  ```json
  {
    "owner": 1,
    "model": "Sensor-M100"
  }
  ```

  Returns:

  - 200 Response if successful

- [GET] /models \
  Get all models.
- [POST] /models \
   Add new model. \
  Params:
  - category (int): id of the category
  - name (str): name of the model
  - energy_cons (float): energy consumption of the model
- [GET] /categories \
  Get all categories.
- [POST] /categories \
   Add new category. \
  Params:
  - name (str): name of the category
- [GET] /getConsumption/models/\<string:model_name\> \
   Get calculated energy consumption for all devices from provided model. \
  Params:
  - model_name (str): name of the model

#### TODO

- [PUT] /devices/\<int:device_id\> \
   Update information about registered device of given id.
  Params:
  - device_id (int): id of the device
- [PUT] /models/\<int:model_id\> \
   Update information about given model.
  Params:
  - model_id (int): id of the model
- [PUT] /categories/\<int:category_id\> \
   Update information about given category.
  Params:
  - category_id (int): id of the category

### Geo-service

- [GET] /positions/\<int:device_id\> \
  Get position of given device. \
  Params:
  - device_id (int): id of the device
- [POST] /positions \
  Add new device's position. \
  Params:
  - device_id (int): id of the existing device
  - pos_x (float): position x of the device
  - pos_y (float): position y of the device
- [GET] /positions/recommend/\<int:user_id> \
  Get recommended position for user's device. \
  Calculated as: x_pos - average of x_positions from all user's devices, y_pos - average of y_positions from all user's devices. Simulates some more complex computations.

  Params:

  - user_id (int): id of the user

#### TODO:

- [GET] /positions/owners/\<int:owner_id\> \
  Get positions of all devices belonging to particular owner.
  Params:
  - owner_id (int): id of the owner
- [PUT] /positions/\<int:device_id\> \
   Update position of given device.
  Params:
  - device_id (int): id of the device

### Stats-service

- [GET] /metrics \
  Get all available metrics.

#### TODO:

Endpoints suggestions to be added once we have the data model clarified.

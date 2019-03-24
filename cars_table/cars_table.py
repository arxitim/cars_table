import csv
import os.path

class CarBase:
    def __init__(self,car_type, brand, photo_file_name, carrying):
        self.car_type = car_type
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying
    def get_photo_file_ext(self):
        ext = os.path.splitext(self.photo_file_name)[1]
        if ext:
            return ext
        else:
            del self
    def __repr__(self):
        return '\n' + str(["{} - {}".format(key, value) for key, value in self.__dict__.items()]) + '\n'



class Car(CarBase):
    def __init__(self,car_type, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(car_type, brand, photo_file_name, carrying)
        self.passenger_seats_count = passenger_seats_count



class Truck(CarBase):
    def __init__(self,car_type, brand, photo_file_name, carrying, body_whl):
        super().__init__(car_type, brand, photo_file_name, carrying)
        try:
            self.body_width, self.body_height, self.body_length = [float(value) for value in body_whl.split('x')]
        except ValueError:
            self.body_width, self.body_height, self.body_length = 0.0, 0.0, 0.0

    def get_body_volume(self):
        return self.body_width * self.body_height * self.body_length


class SpecMachine(CarBase):
    def __init__(self,car_type, brand, photo_file_name, carrying, extra):
        super().__init__(car_type, brand, photo_file_name, carrying)
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=";")
        next(reader)
        for row in reader:
            try:
                if row[0]:
                    car_list.append(row)
            except IndexError:
                continue
    return car_list



car_list = get_car_list("cars_data.csv")
result = []
for car in car_list:

    if car[0] == 'car':
        obj = Car(car_type=car[0], brand=car[1],photo_file_name=car[3], carrying=car[5], passenger_seats_count=car[2])
        result.append(obj)

    elif car[0] == 'truck':
        obj = Truck(car_type=car[0], brand=car[1], photo_file_name=car[3], carrying=car[5], body_whl=car[4])
        result.append(obj)

    elif car[0] == 'spec_machine':
        obj = SpecMachine(car_type=car[0], brand=car[1], photo_file_name=car[3], carrying=car[5], extra=car[6])
        if obj.get_photo_file_ext():
            result.append(obj)
        else:
            del obj
    else: continue

print(result)






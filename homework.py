from typing import Dict, Union

class InfoMessage:
    """Информационное сообщение о тренировке."""

    def __init__(self,
                 training_type: str,
                 duration: int,
                 distance: float,
                 speed: float,
                 calories: float
                ) -> str:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self) -> str:
        return (f'Тип тренировки: {self.training_type}, ' 
              f'Длительность: {self.duration} ч.; '
              f'Дистанция: {self.distance} км; ' 
              f'Ср. скорость: {self.speed} км/ч; ' 
              f'Потрачено ккал: {self.calories}.')


class Training:
    """Базовый класс тренировки."""

    LEN_STEP: float = 0.65
    M_IN_KM: float = 1000
    
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float               
                 ) -> None:                  
        self.action = action
        self.duration = duration
        self.weight = weight
        
    

    def get_distance(self) -> float:
        """Получить дистанцию в км."""

        return self.action * self.LEN_STEP / self.M_IN_KM
        

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""

        return self.get_distance() / self.duration
         

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass 

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""

        return Training.show_training_info()


class Running(Training):
    """Тренировка: бег."""
    
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float
                 ) -> None:
        super().__init__(action, duration, weight) 
                                      
   
    def get_spent_calories(self) -> float:
        
        return (18 * self.get_mean_speed - 20) * self.weight / (
                self.M_IN_KM * 60)

    run_coeff_calorie_1: int = 18
    run_coeff_calorie_2: int = 20
    time_in_hour: int = 60    

          
    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        
        return Running.show_training_info()

class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float,
                ) -> None:
        super().__init__(action, duration, weight)
        self.height = height
    

    def get_spent_calories(self) -> float:

        return (0.035 * self.weight + 
                (self.get_mean_speed**2 // 
                 self.height) * 0.029 * self.weight
               ) * self.duration 
    
    wlk_coeff_calorie_1: float = 0.035
    wlk_coeff_calorie_2: float = 0.029

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке.""" 

        return SportsWalking.show_training_info()   

class Swimming(Training):
    """Тренировка: плавание."""
   
    LEN_STEP: float = 1.38

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: int,
                 count_pool: int                
                ) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool
                            
    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""

        return(self.length_pool * self.count_pool /
               self.M_IN_KM / 
               self.duration
              )
    
    def get_spent_calories(self) -> float:

        return(self.get_mean_speed + 1.1) * 2 * self.weight 


    swm_coeff_calorie_1 = 1.1
    swm_coeff_calorie_2 = 2

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке.""" 

        return Swimming.show_training_info()

def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    
    type_dict : Dict[str, type[Union[Running, Swimming, SportsWalking]]] = {
        'SWM': Swimming, 
        'RUN': Running, 
        'WLK': SportsWalking}

    training = type_dict.get(workout_type)(*data)
                    
def main(training: Training) -> None:
    """Главная функция."""
     
    info_message = InfoMessage.get_message
    print(info_message)
    print(type(Training.get_spent_calories()))


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)


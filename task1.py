class Laser:
    """Базовый класс"""

    def __init__(self, name: str, wavelength: int, FWHM: float, efficiency: float):
        """
        :param name: название лазера
        :param wavelength: длина волны максимума излучения лазера
        :param FWHM: ширина спектра на полувысоте
        :param efficiency: КПД лазера
        """
        self.name = name
        self.wavelength = wavelength
        self.FWHM = FWHM
        self.efficiency = efficiency

    def __str__(self):
        return f"Лазер: {self.name} \nДлина волны: {self.wavelength} нм \nFWHM: {self.FWHM} нм \nКПД: {self.efficiency}%\n"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, wavelength={self.wavelength!r}, FWHM={self.FWHM!r}, " \
               f"efficiency={self.efficiency!r}) "

    def COMD(self):
        """
        COMD - выгорание,плавление зеркала резонатора, что делает лазер полностью нерабочим
        Поэтому его эффективность зануляется, а остальные значения не определены, поскольку такой лазер не излучает
        :return:
        """
        self.efficiency = 0
        self.wavelength = None
        self.FWHM = None

    def rename(self, new_name: str):
        """
        Метод переименовывает лазер, позволяя допистаь особенности лазера по типу COMDа
        :param new_name:
        :return:
        """
        self.name = new_name


class Semiconductor_laser(Laser):
    """Дочерный класс полупроводниковых лазеров"""

    def __init__(self, name: str, wavelength: int, FWHM: float, efficiency: float, number_QW: int, waveguide: float,
                 M2: float):
        """

        :param number_QW: Число квантовых ям в гетероструктуре
        :param waveguide: Ширина волновода (апертура излучения)
        :param M2: параметр расходимости луча, свойственный полупроводниковым лазерам
        """
        super().__init__(name, wavelength, FWHM, efficiency)
        self.number_QW = number_QW
        self.waveguide = waveguide
        self.M2 = M2

    def __str__(self):
        return f"Полупроводниковый лазер: {self.name} \nДлина волны: {self.wavelength} нм \nFWHM: {self.FWHM} нм \nКПД: {self.efficiency}%\n" \
               f"Число квантовых ям: {self.number_QW} \nШирина волновода: {self.waveguide} мкм\nM2: {self.M2}\n"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, wavelength={self.wavelength!r}, FWHM={self.FWHM!r}, " \
               f"efficiency={self.efficiency!r}, number_QW={self.number_QW!r}, waveguide={self.waveguide!r}, M2={self.M2}) "

    def COMD(self):
        """
        Перегружаем метод, поскольку добавляется параметр расходимости луча M2, который тоже необходимо сделать неизвестным
        при сгоревшем неизлучающем лазере
        :return:
        """
        self.efficiency = 0
        self.wavelength = None
        self.FWHM = None
        self.M2 = None


class Gas_laser(Laser):
    """Дочерний класс газовых лазеров"""

    def __init__(self, name: str, wavelength: int, FWHM: float, efficiency: float, gas: str):
        """
        :param gas: газ, составляющий основу лазера
        """
        super().__init__(name, wavelength, FWHM, efficiency)
        self.gas = gas

    def __str__(self):
        return f"Газовый лазер: {self.name} \nДлина волны: {self.wavelength} нм \nFWHM: {self.FWHM} нм \nКПД: {self.efficiency}%" \
               f"\nГаз: {self.gas}\n"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, wavelength={self.wavelength!r}, FWHM={self.FWHM!r}, " \
               f"efficiency={self.efficiency!r}, gas={self.gas!r}) "


if __name__ == "__main__":
    laser_1 = Laser('NL2006-1', 976, 0.6, 97)
    print(laser_1)
    laser_1.COMD()
    laser_1.rename("NL2006-1 COMD")
    print(laser_1)

    laser_2 = Semiconductor_laser("NL2007-1", 976, 0.6, 87, 1, 2, 25)
    print(laser_2)
    laser_2.COMD()
    laser_2.rename("NL2007-1 COMD")
    print(laser_2)

    laser_3 = Gas_laser("MB24", 9400, 100, 17, "CO2")
    print(laser_3)
    # Write your solution here
    # pass

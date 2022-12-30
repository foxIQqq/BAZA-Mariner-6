import math
import matplotlib.pylab as plt


def zakon_vsemirnogo_tagotenia(G, m1, m2, r):
    return G * (m1 * m2 / (r ** 2))


def sila_soprotivleniya_vozduha(Cf, p, V, S):
    return Cf * p * (V ** 2) * S / 2


def sila_prepadstvia_ismeneniyu_uglovoy_skorosti(k, w, p, L):
    return k * (w ** 2) * p * L / 2


def result_sila(alfa, f1, f2):
    return math.sqrt(f1 ** 2 + f2 ** 2 - 2 * math.cos(alfa * math.pi / 180) * f1 * f2)


def ugol(F1, F2, F3):
    return math.acos((F3 ** 2 + F2 ** 2 - F1 ** 2) / (2 * F3 * F2))


def sila_podyoma(alfa, f):
    return f * math.sin(alfa - math.pi / 2)


def skorost_podyoma(fiS, V):
    return V * math.sin((fiS - 90) * math.pi / 180)


def plotnost_vosduha(M, R, T, p0, g, h):
    return p0 * math.exp(- (M * g * h) / (R * T)) * M / (R * T)


def peremeshenie(V0, f, m, t):
    return V0 * t + (f * (t ** 2))/ (m * 2)


def skorost(V0, f, m, t):
    return V0 + f * t / m


def day(t):
    return t / (24 * 60 * 60)


lit = [0]
liV = [0]
m1DO = 16739    # масса 1 ступени и обтикателей
m2D = 29690    # масса 2 ступени без топлива
m2B = 169000    # масса топлива 2 ступени
m3B = 41229    # масса топлива 3 ступени
m3D = 32919    # масса 3 ступени
mM = 2259    # масса маринера
mo = m1DO + m2D + m2B + mM + m3B + m3D
fT1 = 2000000    # тягловая сила 1 ступени
fT2 = 1500000    # тягловая сила 2 ступени
fT3 = 2000000    # тягловая сила 3 ступени
alfa = 0    # угол тклонения ракеты от нормали
Ra12 = 1235.05    # потребление 1 и 2 ступени в секунду
Ra2 = 696.64375    # потребление 2 ступени в секунду
Ra3 = 712.1828125    # потребление 3 ступени в секунду
M0 = 5.9736 * (10 ** 24)     # масса земли
r = 6371000     # радиус земли
G = 6.67 * (10 ** (- 11))      # ргавитационная постоянная
S = 6.05    # периметр поперечного сечения ракеты
Cf1 = 0.82    # коэфициент сопротивления воздуха
M = 0.29    # молярная масса воздуха
R = 8.314    # универсальная газовая постоянная
T = 300    # для упрощения матмодели берём температуру постоянную
V = 0     # скорость ракеты
Vh = 0      # вертикальная скорость ракеты
g = 9.81     # ускорение свободного падения
p0 = 101325    # нормлаьное атмосферное давление
t = 1    # промежуток времени
alfa1 = math.pi
time = 0
h = 0
Vh -= 5 - 5
while h < 2000:
    time += t
    p = plotnost_vosduha(M, R, T, p0, g, h)
    fR = fT1 + fT2 - sila_soprotivleniya_vozduha(Cf1, p, V, S)
    f = fR - mo * g
    V = skorost(V, f, mo, t)
    Vh = V
    h += peremeshenie(Vh, f, mo, t)
    m2B -= Ra12 * t
    mo -= Ra12 * t
    lit.append(time)
    liV.append(V)
d_alfa = 0.73 * t    # на сколько вращать за 1 тик
while h < 35000:
    alfa += d_alfa
    time += t
    p = plotnost_vosduha(M, R, T, p0, g, h)
    f1 = zakon_vsemirnogo_tagotenia(G, M0, mo, r + h)
    fR = fT1 + fT2 - sila_soprotivleniya_vozduha(Cf1, p, V, S)
    f = result_sila(alfa, f1, fR)
    alfa1 = ugol(fR, f1, f)
    fh = sila_podyoma(alfa1, f)
    V = skorost(V, f, mo, t)
    Vh = skorost(Vh, fh, mo, t)
    h += peremeshenie(Vh, fh, mo, t)
    m2B -= Ra12 * t
    mo -= Ra12 * t
    lit.append(time)
    liV.append(V)
print("Угол результирующей силы на момент сброса 1 ступени: ", alfa1 * 180 / math.pi, "скорость на момент сброса 1 ступени: ", V, " Масса на момент сброса 1 ступени: ", mo, " Высота на момент сброса 1 ступени: ", h)
print(time)
mo -= m1DO
d_alfa = - 2.24 * t    # на сколько вращать за 1 тик
while m2B >= Ra2:
    alfa += d_alfa
    time += t
    p = plotnost_vosduha(M, R, T, p0, g, h)
    f1 = zakon_vsemirnogo_tagotenia(G, M0, mo, r + h)
    fR = fT2 - sila_soprotivleniya_vozduha(Cf1, p, V, S)
    f = result_sila(alfa, f1, fR)
    alfa1 = ugol(fR, f1, f)
    fh = sila_podyoma(alfa1, f)
    V = skorost(V, f, mo, t)
    Vh = skorost(Vh, fh, mo, t)
    h += peremeshenie(Vh, fh, mo, t)
    m2B -= Ra2 * t
    mo -= Ra2 * t
    lit.append(time)
    liV.append(V)
print("Угол результирующей силы на момент сброса 2 ступени: ", alfa1 * 180 / math.pi, "скорость на момент сброса 2 ступени: ", V, " Масса на момент сброса 2 ступени: ", mo, " Высота на момент сброса 2 ступени: ", h)
print(time)
mo -= m2D + m2B
d_alfa = 0 * t    # на сколько вращать за 1 тик
while m3B >= Ra3:
    alfa += d_alfa
    time += t
    p = plotnost_vosduha(M, R, T, p0, g, h)
    f1 = zakon_vsemirnogo_tagotenia(G, M0, mo, r + h)
    fR = fT3 - sila_soprotivleniya_vozduha(Cf1, p, V, S)
    f = result_sila(alfa, f1, fR)
    alfa1 = ugol(fR, f1, f)
    fh = sila_podyoma(alfa1, f)
    V = skorost(V, f, mo, t)
    Vh = skorost(Vh, fh, mo, t)
    h += peremeshenie(Vh, fh, mo, t)
    m3B -= Ra3 * t
    mo -= Ra3 * t
    lit.append(time)
    liV.append(V)
print("Угол результирующей силы на момент сброса 3 ступени: ", alfa1 * 180 / math.pi, "скорость на момент сброса 3 ступени: ", V, " Масса на момент сброса 3 ступени: ", mo, " Высота на момент сброса 3 ступени: ", h)
print(time)
t2 = 100
Sx = 0      # пройденный путь
time2 = 0       # время полёта
alfaS = 118      # угол между движением аппарата и направляющей к солнцу
H = 149600000000 + h     # расстояние от солнца до аппарата
V += 2000
while H < 228000000000:
    time2 += t2
    Vh = skorost_podyoma(alfaS, V)
    H += Vh * t2
    Sx += V * t2
print("Аппарат летел до марса ", day(time2), " дней и ", Sx, "метров")
plt.grid()
plt.plot(lit, liV, color='r', label='Python')
plt.xlabel("Время")
plt.ylabel("Скорость")
plt.title("График изменения скорости от времени")
plt.show()
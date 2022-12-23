import math

def Uravnenie_cialkovskogo(Isp, Mf, Mc, g):
    return Isp * g * math.log(Mf / Mc)


def zakon_vsemirnogo_tagotenia(G, m1, m2, r):
    return G * (m1 * m2 / (r ** 2))


def uravnenie_mecherskogo(Fp, F, mp):
    return (Fp + F) / mp


def koedicent_izmemenie_massi(M0, M, T):
    return (M0 - M) / T


def uravnenie_reshoda_massi(M0, k, t):
    return M0 - k * t


def sila_soprotivleniya_vozduha(Cf, p, v, S):
    return Cf * p * (v ** 2) * S / 2


def sila_prepadstvia_ismeneniyu_uglovoy_skorosti(k, w, p, L):
    return k * (w ** 2) * p * L / 2


def result_sila(fi, f1, f2):
    return math.cos(fi) * f1 + math.sqrt(f2 ** 2 - (math.sin(fi) * f1) ** 2)


def sila_podyoma(fi, f):
    return f * math.sin(fi - 90)


def plotnost_vosduha(M, R, T, p0, g, h):
    if h > 52000:
        return 0
    else:
        return p0 * math.exp(- (M * g * h) / (R * T)) * M / (R * T)


def peremeshenie(V0, f, m, t):
    return V0 * t + (f * (t ** 2))/ (m * 2)


def skorost(V0, f, m, t):
    return V0 + f * t / m


Prov = 400
m0E = 3646    # масса 1 ступени
m1G = 128500    # масса 2 ступени с топливом
m1E = 4000    # масса пустой 2 ступени
m2G = 16258    # масса 3 ступени с топливом
m2E = 2631    # масса пустой 3 ступени
mM = 441.8    # масса маринера
mo = m1G + m2G + m0E + mM
fd0 = 1896010    # тягловая сила 1 ступени
fd1 = 428800    # тягловая сила 2 ступени
fd2 = 146022    # тягловая сила 3 ступени
t0 = 179    # время сгорания 1 ступени
t1 = 430    # время сгорания 2 ступени
t2 = 470    # время сгорания 3 ступени
fi = 180    # угол между направлением движения ракеты и нормалью
Ra0 = 466.9746348918849    # потребление 1 ступени в секунду
Ra1 = 95.1431171031456    # потребление 2 ступени в секунду
Ra2 = 28.9936170212766    # потребление 3 ступени в секунду
M0 = 5.9736 * (10 ** 24)     # масса земли
r = 6371000     # радиус земли
G = 6.67 * (10 ** (- 11))      # ргавитационная постоянная
S = 3.05    # периметр поперечного сечения ракеты
Cf = 0.82    # коэфициент сопротивления воздуха
M = 29    # молярная масса воздуха
R = 8.314    # универсальная газовая постоянная
T = 300    # для упрощения матмодели берём температуру постоянную
V = 0     # скорость ракеты
Vh = 0      # вертикальная скорость ракеты
g = 9.81     # ускорение свободного падения
p0 = 101325    # нормлаьное атмосферное давление
t = 1    # промежуток времени
time = 0
h = 0
Vh -= 5 - 5
while h < 16000:
    time += t
    p = plotnost_vosduha(M, R, T, p0, g, h)
    f = fd0 + fd1 - sila_soprotivleniya_vozduha(Cf, p, V, S) - mo * g
    V = skorost(V, f, mo, t)
    Vh = V
    h += peremeshenie(Vh, f, mo, t)
    mo -= Ra0 * t + Ra1 * t
fi1 = 60    # до какого градуса вращать до отброса 1 ступени
dfi = fi1 / (t0 - time)
while time <= t0:
    time += t
    p = plotnost_vosduha(M, R, T, p0, g, h)
    f1 = zakon_vsemirnogo_tagotenia(G, M0, mo, r + h)
    f = result_sila(fi, f1, fd0 + fd1) - sila_soprotivleniya_vozduha(Cf, p, V, S)
    fh = sila_podyoma(fi, f)
    V = skorost(V, f, mo, t)
    Vh = skorost(Vh, fh, mo, t)
    h += peremeshenie(Vh, fh, mo, t)
    mo -= Ra0 * t + Ra1 * t
    fi -= dfi
mo -= m0E
fi2 = 70     # до какого градуса вращать до отброса 2 ступени
dfi = (fi2 - fi1) / (t1 - time)
while time <= t1:
    time += t
    p = plotnost_vosduha(M, R, T, p0, g, h)
    f1 = zakon_vsemirnogo_tagotenia(G, M0, mo, r + h)
    f = result_sila(fi, f1, fd1) - sila_soprotivleniya_vozduha(Cf, p, V, S)
    fh = sila_podyoma(fi, f)
    V = skorost(V, f, mo, t)
    Vh = skorost(Vh, fh, mo, t)
    h += peremeshenie(Vh, fh, mo, t)
    mo -= Ra1 * t
    fi -= dfi
fi3 = 90       # вывод на орбиту
dfi = (fi3 - fi2) / (t1 + t2 - time)
mo -= m1E
while time <= t1 + t2:
    time += t
    p = plotnost_vosduha(M, R, T, p0, g, h)
    f1 = zakon_vsemirnogo_tagotenia(G, M0, mo, r + h)
    f = result_sila(fi, f1, fd2) - sila_soprotivleniya_vozduha(Cf, p, V, S)
    fh = sila_podyoma(fi, f)
    V = skorost(V, f, mo, t)
    Vh = skorost(Vh, fh, mo, t)
    h += peremeshenie(Vh, fh, mo, t)
    mo -= Ra2 * t
    fi -= dfi
mo -= mM
print(V)

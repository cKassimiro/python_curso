from funcoes import func

hora_extra = float(input('Horas extras prestadas: '))
hora_falta = float(input('Horas faltadas: '))

h = func.calc_horas(hora_extra, hora_falta)
func.consulta(h)

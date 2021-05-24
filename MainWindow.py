# Thermistor Calculator

import tkinter as tk
from tkinter import ttk
import generic_liutao as ltgen
from tkinter import messagebox as msg
import math


class MainWindow():

	def __init__(self):
		self.win = tk.Tk()
		self.win.title('ThermCalc')
		self.win.resizable(False, False)
		self.create_widgets()

	def _quit(self):
		self.win.quit()
		self.win.destroy()
		exit()

# the toplevel of about,the information of ThermCalc
	def _about(self):
		win_about = tk.Toplevel()
		win_about.title('About ThermCalc')
		about_name = tk.Label(win_about, text='ThermCalc')
		about_name.config(font=('Arial', 30), foreground='red', width=12)
		about_name.config(pady=5)
		about_name.pack()

		tk.Label(win_about, text='Designed by LiuTao @2020', pady=3).pack()
		tk.Label(win_about, text='E-mail: wxyj3496@126.com', pady=3).pack()


# the function,choose the choise of temptransform

	def temptransCall(self):
		textin = self.temp_enterVar.get()
		textre = self.temp_resultVar

		if textin == '':
			msg.showinfo('ThermCalc Info Box', 'Pleaes input the temperature.')
		# -----------change the unit of temp-----------------------------
		else:
			radSel = self.radVar.get()
			if radSel == 0:
				self.unit_entered.configure(text='C')
				self.unit_result.configure(text='K')
				textre.set(str(round(float(textin) + 273.15, 3)))
				# print(ltgen.is_number('+32'))
			elif radSel == 1:
				self.unit_entered.configure(text='C')
				self.unit_result.configure(text='F')
				textre.set(str(round(float(textin) / 1.8 + 32, 3)))
			elif radSel == 2:
				self.unit_entered.configure(text='K')
				self.unit_result.configure(text='C')
				textre.set(str(round(float(textin) - 273.15, 3)))
			elif radSel == 3:
				self.unit_entered.configure(text='K')
				self.unit_result.configure(text='F')
				textre.set(str(round((float(textin) + 273.15) / 1.8 + 32, 3)))
			elif radSel == 4:
				self.unit_entered.configure(text='F')
				self.unit_result.configure(text='C')
				textre.set(str(round((float(textin) - 32) * 1.8, 3)))
			elif radSel == 5:
				self.unit_entered.configure(text='F')
				self.unit_result.configure(text='K')
				textre.set(str(round((float(textin) - 32) * 1.8 + 273.15, 3)))
			else:
				msg.showinfo('ThermCalc Info Box',\
						'Pleaes select the choice of transform.')

# test the input is float or not
	def testfloat(self, name_entry):
		widget = self.win.nametowidget(name_entry)
		textin = widget.get()

		if ltgen.is_number(textin):
			# msg.showinfo('ThermCalc Info Box','Pleaes input float.')
			return True
		else:
			widget.delete(0, tk.END)
			# msg.showinfo('ThermCalc Info Box','Pleaes input float1.')
			return False

# thefunction of chang the coefficient of NTC resistor
	def changeabc_NTC(self, event):
		choise_res = self.thermreschoise.get()
		a = self.factora_NTC_enterVar
		b = self.factorb_NTC_enterVar
		c = self.factorc_NTC_enterVar
		if choise_res == 'MF501':
			a.set('-6.01188')
			b.set('4622.53337')
			c.set('-86421.72414')
		elif choise_res == 'MF61/MF601':
			a.set('-4.36216')
			b.set('4081.70194')
			c.set('-94033.78039')
		elif choise_res == 'MF51-3000-3.9k':
			a.set('-3.051648504')
			b.set('3776.200666')
			c.set('-119566.8764')
		elif choise_res == 'MF51-3000-8.2k':
			a.set('-2.308490903')
			b.set('3776.200666')
			c.set('-119566.876')
		elif choise_res == 'MF51-3000-18k':
			a.set('-1.5222533')
			b.set('3776.200666')
			c.set('-119566.876')
		elif choise_res == 'MF51-3000-30k':
			a.set('-2.251789232')
			b.set('4271.182215')
			c.set('-148413.1934')
		elif choise_res == 'OtherNTC':
			a.set('-2.251789232')
			b.set('4271.182215')
			c.set('-148413.1934')
			msg.showinfo('ThermCalc Info Box',\
					'Pleaes input the coefficient a,b,c.')

# the function of thermres transform, temp to res

	def temp2restransCall(self):
		temp = self.temp2res_enterVar.get()
		a = self.factora_NTC_enterVar.get()
		b = self.factorb_NTC_enterVar.get()
		c = self.factorc_NTC_enterVar.get()
		upvolt = self.upvolt_enterVar.get()
		upres = self.upres_enterVar.get()
		result_volt = self.temp2volt_result
		if temp == '':
			msg.showinfo('ThermCalc Info Box','Pleaes input the temperature.')
		else:
			if a == '' or b == '' or c == '':
				msg.showinfo('ThermCalc Info Box', \
					'Pleaes input the coefficient a,b,c.')
			else:
				result_res = self.temp2thermres_result
				temp = float(temp)
				a = float(a)
				b = float(b)
				c = float(c)
				T = temp + 273.15
				tempcalc = math.exp(a+b/T+c/(T**2))
				tempcalc = round(tempcalc, 3)
				result_res.set(tempcalc)

			# -----clac the voltage of thermres----
				if upvolt == '' or upres == '':
					msg.showinfo('ThermCalc Info Box','Pleaes input the upvolt or upres.')
				else:
					upvolt = float(upvolt)
					upres = float(upres)*1000
					devvoltcalc = upvolt * tempcalc/(tempcalc+upres)
					devvoltcalc = round(devvoltcalc, 3)
					result_volt.set(devvoltcalc)




# the function of thermres transform, res to temp


	def res2temptransCall(self):
		res = self.res2temp_enterVar.get()
		a = self.factora_NTC_enterVar.get()
		b = self.factorb_NTC_enterVar.get()
		c = self.factorc_NTC_enterVar.get()
		upvolt = self.upvolt_enterVar.get()
		upres = self.upres_enterVar.get()
		result_volt = self.thermres2volt_result


		if res == '':
			msg.showinfo('ThermCalc Info Box', 'Pleaes input the resistor.')
		else:
			if a == '' or b == '' or c == '':
				msg.showinfo('ThermCalc Info Box', \
					'Pleaes input the coefficient a,b,c.')
			else:
				result_temp = self.thermres2temp_result
				res = float(res)
				a = float(a)
				b = float(b)
				c = float(c)
				rescalc = 2*c / (-b+math.sqrt(b*b-4*c*(a-math.log(res, math.e))))-273.15
				rescalc = round(rescalc, 3)
				result_temp.set(rescalc)
				if upvolt == '' or upres == '':
					msg.showinfo('ThermCalc Info Box','Pleaes input the upvolt or upres.')
				else:
					upvolt = float(upvolt)
					upres = float(upres) * 1000
					devvoltcalc = upvolt * res / (res + upres)
					devvoltcalc = round(devvoltcalc, 3)
					result_volt.set(devvoltcalc)

# create the widgets of win(MainWindow)
	def create_widgets(self):
		# =================Menu==========================================
		menu_bar = tk.Menu(self.win)
		self.win.config(menu=menu_bar)

		file_menu = tk.Menu(menu_bar, tearoff=0)
		menu_bar.add_cascade(label='File', menu=file_menu)
		file_menu.add_command(label='Exit', command=self._quit)

		help_menu = tk.Menu(menu_bar, tearoff=0)
		menu_bar.add_cascade(label='Help', menu=help_menu)
		help_menu.add_command(label='About ThermCalc', command=self._about)

	# ================Tabed==========================================
		tabControl = ttk.Notebook(self.win)
		tab_Transform = ttk.Frame(tabControl)
		tabControl.add(tab_Transform, text='Transform')
		tab_Accuracy = ttk.Frame(tabControl)
		tabControl.add(tab_Accuracy, text='Accuracy')

		tabControl.pack(expand=1, fill='both')

		# ===================Transfrom LabFrame==========================

		frame_temptran = ttk.LabelFrame(tab_Transform, text='TempTran',\
			height=2000, width=50)
		frame_temptran.grid(row=0, column=0, padx=3, pady=4)

		frame_thermrestran = ttk.LabelFrame(tab_Transform, text='ThermresTran')
		frame_thermrestran.grid(row=1, column=0, padx=3, pady=4, columnspan=2)

		# ===================widgets of Temp Transform===================

		# -------------------radio choose trans--------------------------
		choise_trans = ['Celsius to Kelvin', 'Celsius to Fahrenheit',\
					'Kelvin to Celsius', 'Kelvin to Fahrenheit',\
					'Fahrenheit to Celsius', 'Fahrenheit to Kelvin']

		self.radVar = tk.IntVar()
		self.radVar.set(0)
		for cho in range(6):
			radTran = tk.Radiobutton(frame_temptran, text=choise_trans[cho],\
				variable=self.radVar, value=cho, command=self.temptransCall)
			radTran.grid(row=cho//2, column=cho % 2*2, sticky='W',columnspan=2)

		# -------------------result of trans----------------------------
		self.temp_enterVar = tk.StringVar()  # define the variable of enter
		self.temp_resultVar = tk.StringVar()  # define the variable of result
		ttk.Label(frame_temptran, text='Input').grid(row=3,\
			column=0, padx=5, columnspan=2, sticky='W')
		ttk.Label(frame_temptran, text='Result').grid(row=3,\
			column=2, padx=5, columnspan=2, sticky='W')

		self.testtemp = self.win.register(self.testfloat)
		self.temp_entered = ttk.Entry(frame_temptran, width=12,\
			textvariable=self.temp_enterVar, validate='focusout',\
			validatecommand=(self.testtemp, '%W'))
		self.temp_entered.grid(row=4, column=0, padx=5, sticky='W')
		temp_transresult = ttk.Entry(frame_temptran, width=12,\
			textvariable=self.temp_resultVar, state='readonly')
		temp_transresult.grid(row=4, column=2, padx=5, sticky='W')

		self.unit_entered = ttk.Label(frame_temptran, text='')
		self.unit_entered.grid(row=4, column=1, sticky='W')
		self.unit_result = ttk.Label(frame_temptran, text='')
		self.unit_result.grid(row=4, column=3, sticky='W')

		self.temp_enterVar.set('')
		self.temp_resultVar.set('')
		ttk.Button(frame_temptran, text='Confirm',\
			command=self.temptransCall).grid(row=5, column=2,\
			sticky='W', padx=5, pady=10)

		# =================widgets of Thermres Transform=================
		self.temp2res_enterVar = tk.StringVar()  # define variable of temp2res
		self.thermreschoise = tk.StringVar()  # define the choise of thermres
		self.temp2thermres_result = tk.StringVar()  # define the result of thermres

		ttk.Label(frame_thermrestran, text='choose the type'\
			).grid(row=0, column=0, padx=5, sticky='W', columnspan=3)

		# --------the choise of thermres----------------------
		thermres_chosen = ttk.Combobox(frame_thermrestran, width=15,\
			textvariable=self.thermreschoise, state='readonly')
		thermres_chosen['value'] = ('MF501', 'MF61/MF601', 'MF51-3000-3.9k',\
			'MF51-3000-8.2k', 'MF51-3000-18k', 'MF51-3000-30k', 'OtherNTC')
		thermres_chosen.current(0)
		thermres_chosen.bind('<<ComboboxSelected>>', self.changeabc_NTC)
		thermres_chosen.grid(row=1, column=0, padx=5, sticky='W',\
			columnspan=2)

		# ----enter the temp and calc the res-----------------
		ttk.Label(frame_thermrestran, text='Temp to Thermres'\
			).grid(row=4, column=0, padx=5, sticky='W', columnspan=3)

		self.temp2res_entered = ttk.Entry(frame_thermrestran, width=12,\
			textvariable=self.temp2res_enterVar, validate='focusout',\
			validatecommand=(self.testtemp, '%W'))
		self.temp2res_entered.grid(row=5, column=0, padx=5, sticky='W')

		ttk.Label(frame_thermrestran, text='C').grid(row=5,\
			column=1, sticky='W')

		temp2res_transresult = ttk.Entry(frame_thermrestran, width=12,\
			textvariable=self.temp2thermres_result, state='readonly')
		temp2res_transresult.grid(row=5, column=2, padx=5, sticky='W')

		ttk.Label(frame_thermrestran, text='OHM').grid(row=5,\
			column=3, sticky='W')

		ttk.Button(frame_thermrestran, text='Confirm',\
			command=self.temp2restransCall).grid(row=6, column=4,\
			sticky='W', padx=5, pady=10)

		# ----enter the res and calc the temp-----------------
		self.res2temp_enterVar = tk.StringVar()  # define the enter of thermres
		self.thermres2temp_result = tk.StringVar()  # define the result of temp
		ttk.Label(frame_thermrestran, text='Thermres to Temp'\
			).grid(row=7, column=0, padx=5, sticky='W', columnspan=3)

		res2temp_entered = ttk.Entry(frame_thermrestran, width=12,\
			textvariable=self.res2temp_enterVar, validate='focusout',\
			validatecommand=(self.testtemp, '%W'))
		res2temp_entered.grid(row=8, column=0, padx=5, sticky='W')
		ttk.Label(frame_thermrestran, text='OHM').grid(row=8,\
			column=1, sticky='W')

		res2temp_transresult = ttk.Entry(frame_thermrestran, width=12,\
			textvariable=self.thermres2temp_result, state='readonly')
		res2temp_transresult.grid(row=8, column=2, padx=5, sticky='W')

		ttk.Label(frame_thermrestran, text='C').grid(row=8,\
			column=3, sticky='W')
		ttk.Button(frame_thermrestran, text='Confirm',\
			command=self.res2temptransCall).grid(row=9, column=4,\
			sticky='W', padx=5, pady=10)

		# ------------enter the vlotage and pull res-------------------
		self.upvolt_enterVar = tk.StringVar()
		self.upres_enterVar = tk.StringVar()
		self.temp2volt_result = tk.StringVar()
		self.thermres2volt_result = tk.StringVar()

		ttk.Label(frame_thermrestran, text='upvoltage').grid(row=0,\
			column=2, padx=5, sticky='W', columnspan=2)
		self.upvoltage_entered = ttk.Entry(frame_thermrestran, width=12,\
			textvariable=self.upvolt_enterVar, validate='focusout',\
			validatecommand=(self.testtemp, '%W'))
		self.upvolt_enterVar.set(5)
		self.upvoltage_entered.grid(row=1, column=2, padx=5, sticky='W')
		ttk.Label(frame_thermrestran, text='V').grid(row=1,\
			column=3, padx=5, sticky='W')

		ttk.Label(frame_thermrestran, text='upresistor').grid(row=0,\
			column=4, padx=5, sticky='W', columnspan=2)
		self.upresistor_entered = ttk.Entry(frame_thermrestran, width=12,\
			textvariable=self.upres_enterVar, validate='focusout',\
			validatecommand=(self.testtemp, '%W'))
		self.upres_enterVar.set(10)
		self.upresistor_entered.grid(row=1, column=4, padx=5, sticky='W')
		ttk.Label(frame_thermrestran, text='kOHM').grid(row=1,\
			column=5, padx=5, sticky='W')

		temp2volt_transresult = ttk.Entry(frame_thermrestran, width=12,\
			textvariable=self.temp2volt_result, state='readonly')
		temp2volt_transresult.grid(row=5, column=4, padx=5, sticky='W')
		ttk.Label(frame_thermrestran, text='V').grid(row=5,\
			column=5, sticky='W')

		thermres2volt_transresult = ttk.Entry(frame_thermrestran, width=12,\
			textvariable=self.thermres2volt_result, state='readonly')
		thermres2volt_transresult.grid(row=8, column=4, padx=5, sticky='W')
		ttk.Label(frame_thermrestran, text='V').grid(row=8,\
			column=5, sticky='W')
		# ---------------the factor of NTC------------------------
		self.factora_NTC_enterVar = tk.StringVar()
		self.factorb_NTC_enterVar = tk.StringVar()
		self.factorc_NTC_enterVar = tk.StringVar()

		ttk.Label(frame_thermrestran, text='a').grid(row=2,\
			column=0, padx=5, sticky='W', columnspan=3)
		ttk.Label(frame_thermrestran, text='b').grid(row=2,\
			column=2, padx=5, sticky='W', columnspan=3)
		ttk.Label(frame_thermrestran, text='c').grid(row=2,\
			column=4, padx=5, sticky='W', columnspan=3)

		self.factora_NTC_entered = ttk.Entry(frame_thermrestran, width=12,\
			textvariable=self.factora_NTC_enterVar, validate='focusout',\
			validatecommand=(self.testtemp, '%W'))
		self.factora_NTC_entered.grid(row=3, column=0, padx=5, sticky='W')
		self.factorb_NTC_entered = ttk.Entry(frame_thermrestran, width=12,\
			textvariable=self.factorb_NTC_enterVar, validate='focusout',\
			validatecommand=(self.testtemp, '%W'))
		self.factorb_NTC_entered.grid(row=3, column=2, padx=5, sticky='W')
		self.factorc_NTC_entered = ttk.Entry(frame_thermrestran, width=12,\
			textvariable=self.factorc_NTC_enterVar, validate='focusout',\
			validatecommand=(self.testtemp, '%W'))
		self.factorc_NTC_entered.grid(row=3, column=4, padx=5, sticky='W')

		self.factora_NTC_enterVar.set('-6.01188')
		self.factorb_NTC_enterVar.set('4622.53337')
		self.factorc_NTC_enterVar.set('-86421.72414')


# =====================================================================
win_main = MainWindow()
win_main.win.mainloop()

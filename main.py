from calc import Calc_block as cal
from log import result_logger as write_log
import data as d_t
import calcul as ca


def button_click():
 j = d_t.data_formatting(ca.input_data())
 calc_result = cal(j)
 ca.view_data(calc_result, 'Ответ:')
 write_log(j, calc_result)

button_click()
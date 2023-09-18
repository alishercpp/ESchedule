from django import template
from display.models import Pupil

register = template.Library()


@register.filter
def dates(dates):
    return dates.get("dates")

@register.filter
def as_object(grade, pid):
    if pid:
        pass
    else:
        pid = 1
    html = ''
    counter = 1
    for i in grade.grades:
        f_name = Pupil.objects.get(pid=i).first_name
        l_name = Pupil.objects.get(pid=i).last_name
        m_name = Pupil.objects.get(pid=i).middle_name
        k = []
        for x in grade.grades[i]:
            print(grade.grades[i][x], type(grade.grades[i][x]))
            if grade.grades[i][x] == "5":
                k.append(f"<td style='width: 1%' value='{grade.grades[i][x]}'><div style='background: #66eda7; width: 100%; height: 20px'></div></td>")
            elif grade.grades[i][x] == "4":
                k.append(f"<td style='width: 1%' style='max-width: 10px;' value='{grade.grades[i][x]}'><div style='background: #ebed66; width: 100%; height: 20px'></div></td>")
            elif grade.grades[i][x] == "3":
                k.append(f"<td style='width: 1%' style='max-width: 10px;' value='{grade.grades[i][x]}'><div style='background: #ed6666; width: 100%; height: 20px'></div></td>")
            elif grade.grades[i][x] == "2":
                k.append(f"<td style='width: 1%' style='max-width: 10px;' value='{grade.grades[i][x]}'><div style='background: black; width: 100%; height: 20px'></div></td>")
            elif grade.grades[i][x] == "1":
                k.append(f"<td style='width: 1%' style='max-width: 10px;' value='{grade.grades[i][x]}'><div style='background: white; width: 100%; height: 20px'></div></td>")    
            else:
                k.append(f"<td style='width: 1%' value='{grade.grades[i][x]}'><div style='background: blue; width: 100%; height: 20px'>{grade.grades[i][x]}</div></td>")
        s = ''
        for j in k:
            s += j
        if i == pid:
            html += f"""
<tr class="table-success">
    <td value={i} class="noscroll1">{counter}</td>
    <td value="{f_name} {l_name} {m_name}" class="noscroll2">{f_name} {l_name}</td>
    PID{i}
</tr>
"""
        else:
            html += f"""
<tr>
    <td style="width: 1%" class="noscroll1">{counter}</td>
    <td class="noscroll2">{f_name} {l_name}</td>
    PID{i}
</tr>
"""         
        html = html.replace(f'PID{i}', s)
        counter += 1
    return html
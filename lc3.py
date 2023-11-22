def cal_da(bp):
    if bp < 10000:
        da_percentage = 5
    elif bp < 30000:
        da_percentage = 7.5
    elif bp < 50000:
        da_percentage = 11
    else:
        da_percentage = 25

    da = (da_percentage / 100) * bp
    return da


def cal_hra(bp):
    if bp < 10000:
        hra_percentage = 2.5
    else:
        hra_percentage = 5

    hra = (hra_percentage / 100) * bp
    return hra


def cal_ma():
    ma = 500
    return ma

def cal_pt(bp):
    pt_percentage = 8
    pt = (pt_percentage / 100) * bp
    return pt

def cal_pf(bp):
    pf_percentage = 11
    pf = (pf_percentage / 100) * bp
    return pf

def cal_it(bp):
    if bp < 30000:
        it_percentage = 0
    else:
        it_percentage = 20

    it = (it_percentage / 100) * bp
    return it

def calGrossSal(bp, da, hra, ma):
    grossSal = bp + da + hra + ma
    return grossSal

def cal_deduction(pt, pf, it):
    deduction = pt + pf + it
    return deduction

def calNetSal(grossSal, deduction):
    netsal = grossSal - deduction
    return netsal

def generate_payslip(employee_name, employee_code, bp):
    da = cal_da(bp)
    hra = cal_hra(bp)
    ma = cal_ma()
    pt = cal_pt(bp)
    pf = cal_pf(bp)
    it = cal_it(bp)
    grossSal = calGrossSal(bp, da, hra, ma)
    deduction = cal_deduction(pt, pf, it)
    netsal = calNetSal(grossSal, deduction)

    print("------- Payslip -------")
    print("Employee Name:", empname)
    print("Employee Code:", empid)
    print("Basic Pay = ", bp)
    print("DA = ", da)
    print("HRA = ", hra)
    print("MA = ", ma)
    print("PT = ", pt)
    print("PF = ", pf)
    print("IT:", it)
    print("Gross Salary = ", grossSal)
    print("Deduction = ", deduction)
    print("Net Salary = ", netsal)

if __name__ == "__main__":
    empname = input("Enter the employee's name: ")
    empid = input("Enter the employee's code: ")
    bp = float(input("Enter the employee's basic pay: "))

    generate_payslip(empname, empid, bp)

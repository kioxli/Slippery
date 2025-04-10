def processBaseString(baseStr):
    """处理基数字符串：负号处理 + 转为0.xx格式（Python版本）"""
    if not baseStr:
        return "0.0"
    sign = "-" if baseStr[0] == "-" else ""
    value = baseStr.lstrip("-")
    return f"{sign}0.{value}"


def parse_line(line):
    """解析每行数据（基数+指数 → 实际数值）"""
    data = line.split()
    eta_base_str, eta_exp, real_base_str, real_exp, imag_base_str, imag_exp = data
    # 处理基数
    eta_base = float(processBaseString(eta_base_str))
    real_base = float(processBaseString(real_base_str))
    imag_base = float(processBaseString(imag_base_str))
    # 计算实际数值
    eta = eta_base * (10 ** int(eta_exp))
    real = real_base * (10 ** int(real_exp))
    imag = imag_base * (10 ** int(imag_exp))
    return eta, real, imag  # 返回三列数据：eta、实部、虚部


def write_to_dat(eta_values, real_values, imag_values, output_path):
    """
    写入三列数据到新的.dat文件（无间隔行）
    :param eta_values: eta值列表
    :param real_values: 实部值列表
    :param imag_values: 虚部值列表
    :param output_path: 输出文件路径
    """
    with open(output_path, 'w') as f:
        for eta, real, imag in zip(eta_values, real_values, imag_values):
            # 格式化为科学计数法（可按需调整格式）
            f.write(f"{eta:.15e} {real:.15e} {imag:.15e}\n")


def read_and_process(file_path):
    """读取原始文件并处理为三列数据"""
    eta_values = []
    real_values = []
    imag_values = []
    with open(file_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if line:  # 跳过空行（原文件可能有间隔行，此处过滤）
                eta, real, imag = parse_line(line)
                eta_values.append(eta)
                real_values.append(real)
                imag_values.append(imag)
    return eta_values, real_values, imag_values


if __name__ == "__main__":
    input_file = "/home/kioxli/桌面/VSCODE/klb_0.100000_reynolds_3851.860000_Mu_profile.dat"       # 原始输入文件路径（含基数+指数）
    output_file = "output.dat"     # 新生成的三列数据文件路径

    # 读取并处理原始数据
    eta, real, imag = read_and_process(input_file)

    # 写入新的.dat文件
    write_to_dat(eta, real, imag, output_file)

    print(f"数据已写入 {output_file}，格式为三列（eta 实部 虚部），无间隔行。")

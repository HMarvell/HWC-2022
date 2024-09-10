resource "local_file" "HWTerra" {
    content = file("${path.module}/HWC-Reader.py")
    filename = "/Users/<user>/Desktop/HWC/HW_Reader.py"
}

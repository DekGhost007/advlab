# นำเข้า library yt_dlp สำหรับดาวน์โหลด YouTube
import yt_dlp


# ฟังก์ชันสำหรับดาวน์โหลดวิดีโอ
def download_video(url):

    # ตั้งค่าการดาวน์โหลด
    ydl_opts = {

        # best = ดาวน์โหลดคุณภาพสูงสุด
        'format': 'best',

        # ตั้งชื่อไฟล์เป็นชื่อวิดีโอ + นามสกุล เช่น MyVideo.mp4
        'outtmpl': '%(title)s.%(ext)s'
    }

    # สร้าง object YoutubeDL โดยใช้ option ด้านบน
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:

        # เริ่มดาวน์โหลด (ต้องส่งเป็น list)
        ydl.download([url])


# จุดเริ่มต้นของโปรแกรม
if __name__ == "__main__":

    # รับลิงก์ YouTube จากผู้ใช้
    link = input("กรุณาใส่ลิงก์ YouTube: ")

    # เรียกฟังก์ชันดาวน์โหลด
    download_video(link)

    # แสดงข้อความเมื่อโหลดเสร็จ
    print("ดาวน์โหลดเสร็จแล้ว!")


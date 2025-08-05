from lunar_python import Solar

def get_day_master(year, month, day, hour):
    # Convert Solar (Gregorian) to Lunar date
    solar = Solar.fromYmdHms(year, month, day, hour, 0, 0)
    lunar = solar.getLunar()

    # Get Day Master (Heavenly Stem of Day Pillar)
    day_gan = lunar.getDayGan()
    day_zhi = lunar.getDayZhi()
    
    return day_gan, day_zhi

# Input from user
print("🔮 Welcome to the Bazi Day Master Finder")
year = int(input("Enter your birth year (e.g. 1998): "))
month = int(input("Enter your birth month (1-12): "))
day = int(input("Enter your birth day (1-31): "))
hour = int(input("Enter your birth hour (0-23): "))

# Get result
gan, zhi = get_day_master(year, month, day, hour)

# Output
print("🧧 Your Day Master is:", gan)
print("🌿 Your full Day Pillar is:", gan + zhi)


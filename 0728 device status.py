import random
from collections import Counter

sn_list = [f"SN_{i+1:03d}" for i in range(10)]
hosts = ["HOST_1", "HOST_2", "HOST_3", "HOST_4"]

status_choices = ["RUN", "IDLE", "LOST"]
test_result_choices = ["PASS", "FAIL", "PENDING"]

machine_table = {}
for idx, sn in enumerate(sn_list):
    host = hosts[idx % len(hosts)]
    status = random.choice(status_choices)
    test_result = random.choice(test_result_choices)
    machine_table[sn] = {
        "HOST": host,
        "STATUS": status,
        "TEST_RESULT": test_result
    }

print("🔧 機器狀態總覽：")
print(f"{'SN':<10}{'HOST':<10}{'STATUS':<12}{'TEST_RESULT'}")
print("-" * 45)
for sn, info in machine_table.items():
    print(f"{sn:<10}{info['HOST']:<10}{info['STATUS']:<12}{info['TEST_RESULT']}")

test_result_counter = Counter(info["TEST_RESULT"] for info in machine_table.values())

print("\n📊 測試結果統計：")
for result in test_result_choices:
    count = test_result_counter.get(result, 0)
    print(f"{result:<8}：{count} 台")

print("\n🔍 輸入 SN 編號查詢（例如 SN_005），輸入 exit 離開。")
while True:
    user_input = input("查詢 SN：").strip().upper()
    if user_input == "EXIT":
        print("✅ 查詢結束，再見！")
        break
    elif user_input in machine_table:
        info = machine_table[user_input]
        print(f"\n📍 SN：{user_input}")
        print(f"    → HOST：{info['HOST']}")
        print(f"    → 狀態：{info['STATUS']}")
        print(f"    → 測試結果：{info['TEST_RESULT']}")
    else:
        print("❌ 無此 SN，請重新輸入。")
        
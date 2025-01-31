### **Test Cases for Car IoT Device Reporting Car Health on a Mobile App**

The **Car IoT device** collects real-time data from the car (like engine status, battery health, fuel levels, etc.) and sends it to the **mobile app**, where the user can view their car’s health.  

---
## **📝 Test Scenarios**
### **1️⃣ Functional Test Cases**
| **Test Case ID** | **Test Scenario** | **Steps** | **Expected Result** |
|-----------------|-----------------|----------|------------------|
| TC_01 | Verify IoT device connectivity with the car | 1. Start the car  2. Check if IoT device connects automatically | Device should connect successfully |
| TC_02 | Verify IoT device syncs data with the app | 1. Connect the device 2. Open the app 3. Check if car health data appears | Car health data should be displayed |
| TC_03 | Verify real-time updates on app | 1. Modify car state (low fuel, overheating) 2. Check if app updates | App should show real-time data |
| TC_04 | Verify data accuracy | 1. Compare IoT device readings with manual readings (e.g., fuel gauge) | Data should match actual car readings |
| TC_05 | Verify notification alerts for warnings | 1. Simulate low battery or overheating 2. Check if the app notifies the user | App should send a push notification |
| TC_06 | Verify app refreshes data periodically | 1. Keep app open 2. Observe data refresh frequency | Data should refresh at regular intervals |
| TC_07 | Verify multiple cars connected to one app | 1. Connect two different cars to the app | The app should switch between cars correctly |

---
### **2️⃣ UI & UX Test Cases**
| **Test Case ID** | **Test Scenario** | **Steps** | **Expected Result** |
|-----------------|-----------------|----------|------------------|
| TC_08 | Verify UI layout for car health display | 1. Open the app 2. Check dashboard layout | Data should be well-organized and readable |
| TC_09 | Verify dark mode support | 1. Enable dark mode on phone 2. Open the app | UI should adapt correctly |
| TC_10 | Verify warning colors for alerts | 1. Trigger a warning (e.g., low battery) 2. Check UI color change | Warnings should be in **red/orange** |
| TC_11 | Verify loading indicators for real-time data | 1. Refresh the app while car is off 2. Check loading indicator | App should show a loading animation |
| TC_12 | Verify app responsiveness | 1. Resize window / change orientation | App should adjust correctly |

---
### **3️⃣ Performance Test Cases**
| **Test Case ID** | **Test Scenario** | **Steps** | **Expected Result** |
|-----------------|-----------------|----------|------------------|
| TC_13 | Verify app response time | 1. Open the app 2. Measure load time | App should load within 2-3 sec |
| TC_14 | Verify data sync speed | 1. Simulate a car state change 2. Measure sync time | Data should sync within 2 sec |
| TC_15 | Verify app performance with weak internet | 1. Connect to 2G network 2. Open the app | App should load with degraded performance but no crash |

---
### **4️⃣ Security Test Cases**
| **Test Case ID** | **Test Scenario** | **Steps** | **Expected Result** |
|-----------------|-----------------|----------|------------------|
| TC_16 | Verify secure data transmission | 1. Capture network traffic between IoT device and app | Data should be encrypted (HTTPS, TLS) |
| TC_17 | Verify authentication before accessing car data | 1. Try to open the app without login | App should require authentication |
| TC_18 | Verify multi-user access restrictions | 1. Log in from two different devices 2. Try to modify settings | Unauthorized changes should be blocked |

---
### **5️⃣ Edge Cases**
| **Test Case ID** | **Test Scenario** | **Steps** | **Expected Result** |
|-----------------|-----------------|----------|------------------|
| TC_19 | Verify behavior when car IoT device is disconnected | 1. Disconnect device 2. Open app | App should show **"Device not connected"** |
| TC_20 | Verify app behavior with incorrect IoT data | 1. Simulate corrupted data from the device | App should **handle errors gracefully** |
| TC_21 | Verify behavior when multiple users access the same car | 1. Log in with two different accounts 2. Check data sync | Data should sync across users without conflict |

---

### **🚀 Summary**
- **Functional Tests** → Ensure correct data sync, notifications, and alerts.  
- **UI/UX Tests** → Verify **user-friendly experience** and warning colors.  
- **Performance Tests** → Measure response times and behavior under load.  
- **Security Tests** → Ensure **encryption, authentication, and multi-user access control**.  
- **Edge Cases** → Test **device disconnections, corrupted data, and multiple users**.

📌 **This ensures the Car IoT device delivers accurate and secure health reports to the app!** 🚗💨
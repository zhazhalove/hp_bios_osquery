# hp_bios_osquery
osqery extension HP BIOS WMI 

# Install

1. Create extension folder for osquery
   
   ``mkdir "C:\Program Files\osquery\Extensions\"``

2. Copy hp_bios_enumeration.py to "C:\Program Files\osquery\Extensions\"
3. Compile hp_bios_enumeration.py file as a binary

   ``cd "C:\Program Files\osquery\Extensions"``
   
   ``pyinstaller --onefile .\hp_bios_enumeration.py``
   
5. Create entry point file for osqueryd to autoload
   
   ``New-Item -Path "C:\Program Files\osquery\extensions.load" -Type File``

   ``Set-Content -Path "C:\Program Files\osquery\extensions.load" -Value "C:\Program Files\osquery\Extensions\dist\hp_bios_enumeration.exe"``

6. Update the osquery.flags

   ``Add-Content -Path "C:\Program Files\osquery\osquery.flags" -Value "--disable_extensions=false"``

   ``Add-Content -Path "C:\Program Files\osquery\osquery.flags" -Value "--extensions_timeout=10"``

   ``Add-Content -Path "C:\Program Files\osquery\osquery.flags" -Value "--extensions_autoload=C:\Program Files\osquery\extensions.load"``

7. Restart osqueryd service

   ``Restart-Service osqueryd``

8. Confirm extension is loaded

   ``osqueryi``

   ``osquery> SELECT * FROM osquery_extensions;``
   
     | uuid | name                          | version | sdk_version | path                   | type      |
     |------|-------------------------------|---------|-------------|------------------------|-----------|
     | 0    | core                          | 5.11.0  | 0.0.0       | \\.\pipe\shell.em      | core      |
     | 9748 | hp_bios_enumeration_extension | 1.0.0   | 1.8.0       | \\.\pipe\shell.em.9748 | extension |

    ``osquery> SELECT * FROM hp_bios_enumeration;``

   | name                                | possible_values                                                 | current_value                       |
   |-------------------------------------|-----------------------------------------------------------------|-------------------------------------|
   | System Management Command           | Disable, Enable                                                 | Enable                              |
   | Fast Boot                           | Disable, Enable                                                 | Enable                              |
   | BIOS Rollback Policy                | Unrestricted Rollback to older BIOS, Restricted Rollback to older BIOS | Unrestricted Rollback to older BIOS |
   | Audio Alerts During Boot            | Disable, Enable                                                 | Enable                              |
  

  

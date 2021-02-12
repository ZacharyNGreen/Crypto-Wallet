#Multi Currency Wallet,

This project is to establish a multicurrency wallet which can be used to send and receive multiple crypto currencies including Ethereum and Bitcoin
The wallet utilizes hd-wallet-derive to create a versatile wallet which can be utilized for multiple currencies. 

The wallet.py file is utilized as the main file which has the wallet

Prior to initializing the wallet you have to have PHP installed on your computer and also must have hd-wallet-derived installed which can be done with the below instructions:




Installing PHP Using the Homebrew Package Manger for Mac


HD Derive Wallet Install for Mac




Step 1 - Environment Setup
The hd-wallet-derive library is written in the PHP language; therefore, you will be required to first set up PHP on your machines before installing and then running the hd-wallet-derive library.
Environment Setup in Microsoft Windows Operating System
For those with a Windows operating system, execute the following steps:


Windows machines do not come with a pre-built PHP and Apache Web Server, and therefore will require both. Luckily, some installers bundle these two together! Visit the XAMPP website and download the installer for Windows; the XAMPP is a popular PHP development environment that is easy to install and configure. Be sure to download version 7, as version 8 can cause issues with the hd-wallet-derive library.
 


Use the XAMPP package to install PHP and its associated dependencies. Keep the defaults for now unless there is a dependency conflict.
 


Then, once the XAMPP package is installed, navigate to the folder where the PHP binaries are located. This should be at C:\xampp\php.
 


Edit the php.ini file (C:\xampp\php\php.ini) using Notepad and add the following line at the end of the file: extension=php_gmp.dll. This will enable a necessary PHP extension that hd-wallet-derive relies on.



Next, you need to update the System Environment Variables and add the path containing the PHP binaries (C:\xampp\php) to the PATH environment variable.


For this particular step, we will use the Windows Command Prompt as Administrator as follows:


In the Cortana search field, type in CMD; you will see the Command Prompt application in the search results, choose the "Run as administrator" option to continue.



You will be asked if you want the Command Prompt to make changes in your system, click on the "Yes" button to continue.



You will be able to run commands as administrator if you see the title Administrator: Command Prompt in the window. In the administrator's prompt, it’ll say Administrator, while other prompts will not.





In this new terminal, type the following command to update the PATH system variable.
setx /M PATH "%PATH%;C:\xampp\php"


If everything was successful, you will see a confirmation message.
!


Test that the newest version of PHP is working. Close all the terminal windows (git-bash and Windows Command Prompt), open a new git-bash terminal windows, and execute the following command.
php -version


If you see the following output, then congratulations! Your machine is now updated to the newest version of PHP!




Troubleshooting

If you do not see something similar to the above output when running  php -version, or if you see the error The data being saved is truncated to 1024 characters, then your environement variables may not be set correctly. Perform the following steps to make sure your environment variables are correctly set:


Click the Windows search and search for System Properties or Edit System, then launch the application.


Next at the bottom of the dialog click Environment variables.


Then under System Variables find the Path variable and click edit.


Now click New and enter your XAMP path, e.g.  C:\xampp\php.


Finish by clicking OK on each window.


  


Environment Setup in macOS Operating System
For those using macOS, execute the following steps:


macOS users will need to update their machine's prebuilt version of PHP to the full version using a package manager for macOS called Homebrew.


To do this, visit the Homebrew website and install Homebrew using the given install command.



Once Homebrew is installed, execute the following command in your terminal. This should install the latest version of PHP (7.3 at this current time).
brew install php@7.3


Next, execute the command appropriate for your system:


macOS Catalina and above (zsh shell):
echo "export PATH=/usr/local/opt/php@7.3/bin:$PATH" >> ~/.zshrc


Versions prior to macOS Catalina (bash shell):
echo "export PATH=/usr/local/opt/php@7.3/bin:$PATH" >> ~/.bash_profile


Note: If you are on macOS Catalina and up (10.15+), your default shell is now zsh, instead of bash as in previous versions. No worries, however, since zsh can handle the same tasks. If you have yet to upgrade to Catalina, you will be using bash as your default shell, which will affect the commands you need to run. Make sure you are running the commands appropriate for your system!




Close the terminal.


Open a NEW terminal, then verify that PHP version 7.3 is the current version in your system by executing the following command:
php -version


If you see the following output, then congratulations! Your machine is now updated to the newest version of PHP!





Step 2 - Installing hd-wallet-derive
With the latest version of PHP installed on our machines, we can now proceed to the installation of the hd-wallet-derive library.
Installation


Begin by opening a fresh terminal. Windows users must open their terminal as administator as follows:


Input C:\Program Files\Git\bin\bash.exe directly into the system search bar and launch the program as Administrator from the resulting menu.


This step is required or the installation will fail!







With your terminal open as indicated for your operating system, cd into your `Blockchain-Tools folder and run the following code:
  git clone https://github.com/dan-da/hd-wallet-derive
  cd hd-wallet-derive
  curl https://getcomposer.org/installer -o installer.php
  php installer.php
  php composer.phar install


You should now have a folder called hd-wallet-derive containing the PHP library!

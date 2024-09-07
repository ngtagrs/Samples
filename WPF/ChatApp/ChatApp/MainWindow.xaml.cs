using System;
using System.Collections.ObjectModel;
using System.Windows;

namespace ChatApp
{
    public partial class MainWindow : Window
    {
        private bool isDarkMode = true;
        public ObservableCollection<ChatMessage> ChatMessages { get; set; }

        public MainWindow()
        {
            InitializeComponent();
            ChatMessages = new ObservableCollection<ChatMessage>();
            ChatListBox.ItemsSource = ChatMessages;
        }

        private void SendButton_Click(object sender, RoutedEventArgs e)
        {
            string userInput = ChatInputTextBox.Text.Trim();
            if (!string.IsNullOrEmpty(userInput))
            {
                ChatMessages.Add(new ChatMessage { Role = "User", Message = userInput });
                ChatInputTextBox.Clear();
                ChatMessages.Add(new ChatMessage { Role = "System", Message = $"Echo: {userInput}" });
            }
        }

        private void ToggleThemeButton_Click(object sender, RoutedEventArgs e)
        {
            if (isDarkMode)
            {
                // Lightモードに切り替え
                var lightTheme = new ResourceDictionary { Source = new Uri("LightTheme.xaml", UriKind.Relative) };
                //Application.Current.Resources.MergedDictionaries[0] = lightTheme;
                isDarkMode = false;
            }
            else
            {
                // Darkモードに切り替え
                var darkTheme = new ResourceDictionary { Source = new Uri("DarkTheme.xaml", UriKind.Relative) };
                //Application.Current.Resources.MergedDictionaries[0] = darkTheme;
                isDarkMode = true;
            }
        }
    }

    public class ChatMessage
    {
        public string Role { get; set; }
        public string Message { get; set; }
        public bool IsUserMessage => Role == "User";
    }
}

import sys,signal

def keyboard_interrupt_handler(signal, frame):
    print("Прерывание обработано. Клавиша нажата.")
    # Дополнительные действия при обработке прерывания
    
# Регистрируем обработчик прерывания
signal.signal(signal.SIGINT, keyboard_interrupt_handler)

# Ждем нажатия клавиши для выхода
print("Для выхода нажмите Ctrl+C")
try:
    while True:
        pass
except KeyboardInterrupt:
    print("\nПрограмма завершена.")
    sys.exit(0)
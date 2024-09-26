from core.base import Base

class Test(Base):
    def initialize(self):
        print("Inicializando programa...")

    def update(self):
        self.input.update()

        if self.input.quit:
            self.running = False
        pass

# Inicia e executa o programa
Test().run()
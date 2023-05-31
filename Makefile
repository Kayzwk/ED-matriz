# Variáveis
ifeq ($(OS),Windows_NT)
    EXECUTABLE = dist/index.exe
else
    EXECUTABLE = dist/index
endif

# Comandos
.PHONY: run
run: $(EXECUTABLE)
	$(EXECUTABLE)

# Limpar os arquivos gerados
.PHONY: clean
clean:
	rm -rf dist

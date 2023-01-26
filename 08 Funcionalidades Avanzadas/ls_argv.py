import sys
from pathlib import Path

print(f"El contenido de argv es: {sys.argv}")

if (args_count := len(sys.argv)) > 2:
    print(f"Se esperaba un argumento, no {args_count - 1}")
    raise SystemExit(2)
elif args_count < 2:
    print("Se debe indicar el directorio")
    raise SystemExit(2)

target_dir: Path = Path(sys.argv[1])

if not target_dir.is_dir():
    print(f"El directorio {sys.argv[1]} no existe")
    raise SystemExit(1)

for entry in target_dir.iterdir():
    print(entry.name)
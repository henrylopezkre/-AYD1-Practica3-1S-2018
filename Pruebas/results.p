set terminal png size 600

set output "index.png"

set title "100 peticiones, 20 peticiones concurrentes"

set size ratio 0.6

set grid y

set xlabel "Peticiones"

set ylabel "Tiempo de respuesta (ms)"

plot "index.tsv" using 9 smooth sbezier with lines title "http://127.0.0.1/index"
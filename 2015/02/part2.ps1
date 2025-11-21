$inputs = Get-Content .\02\input.txt

$ribbon = 0
$inputs | ForEach-Object {
    $dimenstions = $_ -split 'x'

    $l = [int]$dimenstions[0]
    $w = [int]$dimenstions[1]
    $h = [int]$dimenstions[2]

    $sortedDimensions =  ($l, $w, $h) | Sort-Object { $_ }

    $wrap = $sortedDimensions[0] * 2 + $sortedDimensions[1] * 2
    $bow = $l * $w * $h

    $ribbon += ($wrap + $bow)
}

$ribbon
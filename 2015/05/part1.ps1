$inputs = Get-Content .\05\input.txt

$niceString = 0
$inputs | ForEach-Object {
    $vowCheck = $false
    $doubleCheck = $false
    $seqCheck = $false

    $prevLetter = ''
    $vowCount = 0
    [char[]]$_ | ForEach-Object {
        if ($_ -in ('a', 'e', 'i', 'o', 'u'))
        {
            $vowCount++
        }

        if ($_ -eq $prevLetter)
        {
            $doubleCheck = $true
        }

        $prevLetter = $_
    }

    if ($vowCount -ge 3)
    {
        $vowCheck = $true
    }

    if ($_ -notmatch '(ab)|(cd)|(pq)|(xy)')
    {
        $seqCheck = $true
    }

    if ($seqCheck -and $vowCheck -and $doubleCheck)
    {
        $niceString++
    }
}

$niceString

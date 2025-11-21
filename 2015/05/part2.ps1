$inputs = Get-Content .\2015\05\input.txt

$niceString = 0
$inputs | ForEach-Object {
    $charArray = [char[]]$_

    $pairCheck = $false
    $repeatCheck = $false

    $hashPair = @{}
    for ($i = 0; $i -lt ($charArray.count ); $i++)
    {
        if (-not $hashPair.ContainsKey($charArray[$i] + $charArray[$i + 1]))
        {
            $hashPair.($charArray[$i] + $charArray[$i + 1]) = $i
        }
        elseif ($i -ge ($hashPair.($charArray[$i] + $charArray[$i + 1]) + 2))
        {
            $pairCheck = $true
        }

        if ($charArray[$i] -eq $charArray[$i+2])
        {
            $repeatCheck = $true
        }
    }

    if ($pairCheck -and $repeatCheck)
    {
        $niceString++
    }
}

$niceString

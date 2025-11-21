$inputs = Get-Content .\2015\03\input.txt

$coordsSanta = [System.Management.Automation.Host.coordinates]::new(0, 0)
$coordsRoboSanta = [System.Management.Automation.Host.coordinates]::new(0, 0)
$coordHash = @{$coordsSanta.ToString() = 0 }

$i = 0
foreach ($char in [char[]]$inputs)
{
    if ($i % 2 -eq 0)
    {
        $coordsVar = 'coordsSanta'
    }
    else
    {
        $coordsVar = 'coordsRoboSanta'
    }

    if ($char -eq '>')
    {
        (Get-Variable -Name $coordsVar -ValueOnly).X++

    }

    if ($char -eq '<')
    {
        (Get-Variable -Name $coordsVar -ValueOnly).X--
    }

    if ($char -eq '^')
    {
        (Get-Variable -Name $coordsVar -ValueOnly).Y++
    }

    if ($char -eq 'v')
    {
        (Get-Variable -Name $coordsVar -ValueOnly).Y--
    }

    $coordHash.($coordsSanta.ToString()) = 0
    $coordHash.($coordsRoboSanta.ToString()) = 0

    $i++
}

$coordHash.Count
$inputs = Get-Content .\2015\04\input.txt

for ($i = 0; $i -lt 1000000; $i++)
{

    $someString = $inputs + $i
    $md5 = [System.Security.Cryptography.MD5CryptoServiceProvider]::new()
    $utf8 = [System.Text.UTF8Encoding]::new()
    $hash = [System.BitConverter]::ToString($md5.ComputeHash($utf8.GetBytes($someString)))

    if ($hash.Substring(0, 7) -eq '00-00-0')
    {
        return $i
    }
}
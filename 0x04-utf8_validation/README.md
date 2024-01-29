<h3>Validate whether a data set is true UTF-8 encoding</h3>

<ul>
    <li>
        Return: True if data is a valid UTF-8 encoding, else return False
    </li>
    <li>
        A character in UTF-8 can be 1 to 4 bytes long
    </li>
    <li>
        The data set can contain multiple characters
    </li>
    <li>
        The data will be represented by a list of integers
    </li>
    <li>
        Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each
        integer
    </li>
</ul>
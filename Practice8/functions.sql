CREATE OR REPLACE FUNCTION insert_many_users(
    p_usernames TEXT[],
    p_phones TEXT[]
)
RETURNS TEXT
LANGUAGE plpgsql
AS $$
DECLARE
    i INT;
    current_name TEXT;
    current_phone TEXT;
    invalid_data TEXT := '';
BEGIN
    IF array_length(p_usernames, 1) IS DISTINCT FROM array_length(p_phones, 1) THEN
        RETURN 'Error: usernames and phones count do not match';
    END IF;

    FOR i IN 1 .. array_length(p_usernames, 1)
    LOOP
        current_name := trim(p_usernames[i]);
        current_phone := trim(p_phones[i]);

        IF current_phone ~ '^\+7\d{10}$' THEN
            IF EXISTS (
                SELECT 1 FROM phonebook WHERE username = current_name
            ) THEN
                UPDATE phonebook
                SET phone = current_phone
                WHERE username = current_name;
            ELSE
                INSERT INTO phonebook(username, phone)
                VALUES (current_name, current_phone);
            END IF;
        ELSE
            invalid_data := invalid_data || format('[%s: %s] ', current_name, current_phone);
        END IF;
    END LOOP;

    RETURN invalid_data;
END;
$$;
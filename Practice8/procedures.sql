CREATE OR REPLACE PROCEDURE insert_or_update_user(
    p_username VARCHAR(100),
    p_phone VARCHAR(20)
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (
        SELECT 1 FROM phonebook WHERE username = p_username
    ) THEN
        UPDATE phonebook
        SET phone = p_phone
        WHERE username = p_username;
    ELSE
        INSERT INTO phonebook(username, phone)
        VALUES (p_username, p_phone);
    END IF;
END;
$$;


CREATE OR REPLACE PROCEDURE insert_many_users(
    p_usernames TEXT[],
    p_phones TEXT[],
    INOUT p_invalid_data TEXT DEFAULT ''
)
LANGUAGE plpgsql
AS $$
DECLARE
    i INT;
    current_name TEXT;
    current_phone TEXT;
BEGIN
    -- проверка, что длины массивов совпадают
    IF array_length(p_usernames, 1) IS DISTINCT FROM array_length(p_phones, 1) THEN
        p_invalid_data := 'Error: usernames and phones count do not match';
        RETURN;
    END IF;

    FOR i IN 1 .. array_length(p_usernames, 1)
    LOOP
        current_name := trim(p_usernames[i]);
        current_phone := trim(p_phones[i]);

        -- валидация телефона: только формат +7XXXXXXXXXX
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
            p_invalid_data := p_invalid_data ||
                format('[%s: %s] ', current_name, current_phone);
        END IF;
    END LOOP;
END;
$$;


CREATE OR REPLACE PROCEDURE delete_contact_by_value(
    p_value VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM phonebook
    WHERE username = p_value OR phone = p_value;
END;
$$;